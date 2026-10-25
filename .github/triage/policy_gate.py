#!/usr/bin/env python3
"""Deterministic policy gate, run in the threat-detection job before any write.

Re-checks every output the agent proposed with the same code the skill tells
the agent to run, so these rules are enforced rather than only instructed:

- labels: allowlist, at most 3, one type label, `invalid` alone, and a
  `duplicate` label only with a comment naming the earlier issue as #NNNN;
- comments: at most 1, and `check_comment.py` must pass (links only to Rich
  files on master, never an issue/PR/discussion URL; code parses; footer);
- cited issues: every #N, GH-N and owner/repo#N for this repository in a
  comment (outside code) is looked up, and the comment is refused if that
  issue's text addresses automated tools or redirects readers (build_index.py's
  quarantine rules). A replay looks in the frozen snapshot plus the case's
  planted entries as of the case's filing, relative to the working directory
  (the gate's checkout); any other run fetches the issue from the API. A
  number that cannot be found or fetched refuses the comment, and so does a
  reference to another repository's issue or one written as an HTML entity;
- an issue opened by a maintainer (OWNER, MEMBER or COLLABORATOR, after the
  replay marker restores the filed role) gets no label and no comment;
- output types: only add_labels, add_comment, noop and the report types that
  can no longer open issues (report_missing_tool, report_missing_data,
  report_incomplete, and gh-aw's older names missing_tool and missing_data)
  pass; any other type is refused, even if gh-aw would accept it;
- the kill switch: if TRIAGE_AGENT_ENABLED is "false" (in any case; passed
  from the repository variable), nothing is written, even by a run that was
  already past activation when the switch was set.

Any violation, or a missing agent output file, exits 1: the detection job
fails, and gh-aw's safe_outputs job (which needs detection to succeed) writes
nothing.

  python policy_gate.py AGENT_OUTPUT_JSON GITHUB_EVENT_JSON
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, "..", "..", ".claude", "skills", "rich-triage", "scripts")
sys.path.insert(0, SCRIPTS)
os.environ.setdefault("RICH_TRIAGE_TRACE", os.devnull)

sys.path.insert(0, HERE)

import build_index  # noqa: E402
import check_comment  # noqa: E402
import validate_labels  # noqa: E402

MAINTAINERS = {"OWNER", "MEMBER", "COLLABORATOR"}
MARKER = build_index.MARKER
# Issue references GitHub links, outside code: #N, GH-N, owner/repo#N. A
# leading zero or a trailing letter is not a reference, and a 6 or 8 digit #N
# is read as a hex colour (#808080), so neither is looked up.
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?(^ {0,3}\1[ \t]*$|\Z)", re.M | re.S)
CODE_SPAN = re.compile(r"(`+)(?!`).+?(?<!`)\1(?!`)", re.S)
CITED = re.compile(r"(?<![\w&/])#(?!0)(\d+)(?!\w)")
GH_REF = re.compile(r"(?<![\w-])GH-(?!0)(\d+)(?!\w)", re.I)
REPO_REF = re.compile(r"(?<![\w./-])([A-Za-z0-9][\w.-]*/[\w.-]+)#(?!0)(\d+)(?!\w)")
ENTITY_REF = re.compile(r"&(#0*35|#x0*23|num);\s*\d", re.I)
GOLDEN = os.path.join("evals", "golden")
# The safe-output types this workflow may emit (rich-triage.lock.yml's
# safe-outputs config), plus gh-aw's legacy aliases for the two report types.
ALLOWED_TYPES = {"add_labels", "add_comment", "noop", "report_missing_tool", "report_missing_data",
                 "report_incomplete", "missing_tool", "missing_data"}


def replay_marker(issue):
    """The replay marker, honoured only on OWNER-authored issues (as in the prep step)."""
    m = MARKER.search(issue.get("body") or "")
    return m if m and issue.get("author_association") == "OWNER" else None


def filed_role(issue):
    """The author role as filed (the triage prep step applies the same rule)."""
    m = replay_marker(issue)
    return m.group(3) if m else issue.get("author_association")


class SameHost(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only over https on the same host, so the token never leaves the API."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new, old = urllib.parse.urlsplit(newurl), urllib.parse.urlsplit(req.full_url)
        if new.scheme != "https" or new.netloc != old.netloc:
            raise urllib.error.HTTPError(newurl, code, "redirect off the API host or off https", headers, fp)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_issue(n):
    """Issue #n of this repository, from the API. The detection job's token has
    only contents: read, so a 401/403/404 is retried once without it (the
    repository is public)."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN is not set")
    if not os.environ.get("GITHUB_REPOSITORY"):
        raise ValueError("GITHUB_REPOSITORY is not set")
    api = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    url = f"{api}/repos/{os.environ['GITHUB_REPOSITORY']}/issues/{n}"

    def get(auth):
        headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        if auth:
            headers["Authorization"] = f"Bearer {auth}"
        with urllib.request.build_opener(SameHost).open(urllib.request.Request(url, headers=headers),
                                                        timeout=15) as resp:
            return json.load(resp)

    try:
        return get(token)
    except urllib.error.HTTPError as e:
        if e.code not in (401, 403, 404):
            raise
    return get(None)


def replay_index(case, filed):
    """The replayed case's index source as of its filing: the snapshot plus its planted entries."""
    index = json.load(open(os.path.join(GOLDEN, "issues_index.json"), encoding="utf-8"))
    planted = os.path.join(GOLDEN, "adversarial", case, "planted_index.json")
    if build_index.CASE_ID.fullmatch(case) and os.path.exists(planted):
        index += json.load(open(planted, encoding="utf-8"))
    return {r["number"]: r for r in build_index.rewind(index, filed)}


def references(comment):
    """(issue numbers in this repository, problems) for one comment, outside code."""
    text = CODE_SPAN.sub(" ", FENCE.sub("\n", comment))
    numbers = {int(n) for n in CITED.findall(text) if len(n) not in (6, 8)}
    numbers |= {int(n) for n in GH_REF.findall(text)}
    problems = []
    for repo, n in REPO_REF.findall(text):
        if repo.lower() == build_index.this_repo():
            numbers.add(int(n))
        else:
            problems.append(f"comment references another repository's issue {repo}#{n}")
    if ENTITY_REF.search(text):
        problems.append("comment writes an issue reference as an HTML entity")
    return numbers, problems


def cited_problems(comments, issue):
    """Refuse a comment that cites an issue the prep step would quarantine."""
    numbers, problems = set(), []
    for c in comments:
        found, refused = references(c)
        numbers |= found
        problems += refused
    if not numbers:
        return problems
    m = replay_marker(issue)
    index = None
    for n in sorted(numbers):
        try:
            if m:
                index = index if index is not None else replay_index(m.group(1), m.group(2))
                if n not in index:
                    raise LookupError("not in the replay index as of the case's filing")
                r = index[n]
            else:
                r = fetch_issue(n)
            r = {"title": r.get("title"), "body": r.get("body")}
        except Exception as e:  # noqa: BLE001  any failure refuses the comment
            problems.append(f"could not check cited #{n}: {e}")
            continue
        if build_index.addresses_tools(r) or build_index.redirects_readers(r):
            problems.append(f"comment cites #{n}, whose text redirects readers or addresses automated tools")
    return problems


def gate(items, issue):
    problems = [f"output type {i.get('type')!r} is not allowed" for i in items
                if i.get("type") not in ALLOWED_TYPES]
    labels = [l["name"] if isinstance(l, dict) else l
              for i in items if i.get("type") == "add_labels" for l in i.get("labels", [])]
    comments = [i.get("body") or "" for i in items if i.get("type") == "add_comment"]
    if labels:
        problems += [f"labels: {e}" for e in validate_labels.validate(labels)]
    if sum(1 for i in items if i.get("type") == "add_labels") > 1:
        problems.append("more than one add_labels call")
    if len(comments) > 1:
        problems.append(f"{len(comments)} comments; at most 1")
    for c in comments:
        problems += [f"comment: {p}" for p in check_comment.check(c)]
    problems += cited_problems(comments, issue)
    if "duplicate" in labels and not any(re.search(r"#\d+", c) for c in comments):
        problems.append("duplicate label without a comment naming the earlier issue")
    if filed_role(issue) in MAINTAINERS and (labels or comments):
        problems.append("issue opened by a maintainer: no label or comment allowed")
    return problems


def main():
    issue = json.load(open(sys.argv[2])).get("issue", {})
    # The gate step only runs when the agent declared outputs, so a missing
    # output file is an anomaly (e.g. a failed artifact download): fail closed.
    if not os.path.exists(sys.argv[1]):
        items, problems = [], [f"agent output {sys.argv[1]} is missing"]
    else:
        items = json.load(open(sys.argv[1])).get("items", [])
        problems = gate(items, issue)
    if (os.environ.get("TRIAGE_AGENT_ENABLED") or "").strip().lower() == "false":
        problems.append("kill switch is on (TRIAGE_AGENT_ENABLED=false)")
    print(json.dumps({"ok": not problems, "items": len(items), "problems": problems}, indent=2))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
