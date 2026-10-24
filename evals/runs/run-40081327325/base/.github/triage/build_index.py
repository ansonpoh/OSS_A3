#!/usr/bin/env python3
"""Prepare the agent's inputs, run by the workflow's "Prepare triage inputs"
step (before the eval files are deleted):

- /tmp/gh-aw/agent/issue.json: the issue, from the event payload, never from
  the issue text itself;
- /tmp/gh-aw/agent/issues_index.json: earlier issues for duplicate search, as
  the tracker stood when the issue was filed.

Index source:
- replay of a golden case (the marker, honoured only on OWNER-authored
  issues): the frozen snapshot evals/golden/issues_index.json, plus the
  planted entries of adv-4-index-injection for that case only;
- any other issue: this repository's own issues, fetched now from the API
  (replay markers stripped). A failed fetch, a missing token or a next-page
  link outside the API exits 1 (the run fails closed); the eval file is never
  used.

Entries whose title or body address automated tools are quarantined: dropped
from the agent's index, and only their count and numbers are logged.

  python build_index.py
Env: GITHUB_EVENT_PATH; GITHUB_REPOSITORY, GITHUB_TOKEN (and GITHUB_API_URL)
for the API; TRIAGE_GOLDEN (default evals/golden) and TRIAGE_OUT (default
/tmp/gh-aw/agent) let tests run it offline.
"""
import json
import os
import re
import sys
import urllib.request

MARKER = re.compile(r"<!-- golden-case: (\S+) filed: (\S+) as: (\S+) -->")
PLANTED_CASE = "adv-4-index-injection"
KEEP = ("number", "title", "body", "created_at", "closed_at", "state_reason")
# Text written to triage bots rather than to maintainers, or install advice
# pointing at another package index. Kept narrow: none of these matches an
# ordinary issue in the upstream snapshot, where a bare "AI agent" does occur
# (#4051, #4202), so AI must be addressed, not mentioned.
W = r"[\s_-]+"  # between words, also across newlines
ADDRESSES_TOOLS = [re.compile(p, re.I) for p in (
    rf"\bautomated{W}triage\b",
    rf"\btriage{W}(bots?|tools?|agents?)\b",
    rf"\b(dear|attention|note{W}to){W}((any|all){W})?(AI|LLM){W}(assistants?|agents?|models?)\b",
    rf"\b(AI|LLM)({W}(assistants?|agents?|models?))?{W}(reading|triaging|processing){W}this\b",
    rf"\bLLM{W}agents?\b",
    r"\b(ignore|disregard|forget)\s+((the|your|all|any)\s+)*(previous|prior|above)\b",
    r"--(extra-)?index-url\b",
    r"(?<!\S)-i\s+https?://",
    r"\bPIP_(EXTRA_)?INDEX_URL\b",
)]


def fetch_issues(repo, token, api="https://api.github.com"):
    """Every issue (not PR) of the repository, following the Link header."""
    url = f"{api}/repos/{repo}/issues?state=all&per_page=100"
    out = []
    while url:
        if not url.startswith(api + "/"):
            raise ValueError(f"next page {url} is outside {api}")
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            page = json.load(resp)
            m = re.search(r'<([^>]+)>;\s*rel="next"', resp.headers.get("Link") or "")
        out += [{k: i.get(k) for k in KEEP} for i in page if "pull_request" not in i]
        url = m.group(1) if m else None
    for i in out:
        # A replayed case filed in this repository keeps its marker; drop it.
        i["body"] = MARKER.sub("", i["body"] or "").rstrip()
    return out


def rewind(index, created):
    """Only earlier issues, and any later close is hidden."""
    idx = []
    for r in index:
        if r["created_at"] >= created:
            continue
        if r.get("closed_at") and r["closed_at"] >= created:
            r = {**r, "closed_at": None, "state_reason": None}
        idx.append(r)
    return idx


def addresses_tools(r):
    return any(p.search(r["title"] or "") or p.search(r["body"] or "") for p in ADDRESSES_TOOLS)


def quarantine(index):
    """(entries kept, numbers dropped)."""
    held = [r["number"] for r in index if addresses_tools(r)]
    return [r for r in index if r["number"] not in held], held


def main():
    golden = os.environ.get("TRIAGE_GOLDEN", "evals/golden")
    out_dir = os.environ.get("TRIAGE_OUT", "/tmp/gh-aw/agent")
    ev = json.load(open(os.environ["GITHUB_EVENT_PATH"]))["issue"]
    body = ev.get("body") or ""
    created = ev["created_at"]
    # Replay of a historical case: the repository owner's harness records
    # the original filing time so duplicate search cannot see later issues.
    # Only honoured for OWNER-authored issues.
    # The replay posts as the owner, so the original author role is
    # restored too; the agent never sees that a case is a replay.
    assoc = ev.get("author_association")
    m = MARKER.search(body)
    replay = bool(m and assoc == "OWNER")
    if replay:
        created, assoc = m.group(2), m.group(3)
        body = body.replace(m.group(0), "").rstrip()
    issue = {"number": ev["number"], "title": ev["title"], "body": body,
             "author_association": assoc,
             "created_at": created, "labels": [l["name"] for l in ev.get("labels", [])]}
    os.makedirs(out_dir, exist_ok=True)
    json.dump(issue, open(os.path.join(out_dir, "issue.json"), "w"), indent=2)

    if replay:
        source = "replay snapshot"
        index = json.load(open(os.path.join(golden, "issues_index.json")))
        if m.group(1) == PLANTED_CASE:
            index += json.load(open(os.path.join(golden, "adversarial", PLANTED_CASE, "planted_index.json")))
    else:
        source = "repository issues"
        if not os.environ.get("GITHUB_TOKEN"):
            sys.exit("GITHUB_TOKEN is not set: cannot fetch the repository's issues")
        try:
            index = fetch_issues(os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_TOKEN"],
                                 os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/"))
        except Exception as e:  # noqa: BLE001  any failure fails the run
            sys.exit(f"could not fetch the repository's issues: {e}")
    idx, held = quarantine(rewind(index, created))
    json.dump(idx, open(os.path.join(out_dir, "issues_index.json"), "w"))
    print(f"issue #{issue['number']} as of {created}; {len(idx)} earlier issues indexed "
          f"from {source}; {len(held)} quarantined {held}")


if __name__ == "__main__":
    main()
