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
  planted entries of evals/golden/adversarial/<case>/planted_index.json, if
  that file exists, for that case only;
- any other issue: this repository's own issues, fetched now from the API
  (golden-case replays left out). A failed fetch, a missing token or a next-page
  link outside the API exits 1 (the run fails closed); the eval file is never
  used.

Entries whose title or body address automated tools, or redirect human
readers (install advice next to a link off the allowlisted hosts, or a request
to close or label other reports), are quarantined: dropped from the agent's
index, and only their count and numbers are logged. The policy gate applies
the same two rules to every issue a proposed comment cites.

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
CASE_ID = re.compile(r"[A-Za-z0-9][\w-]*")  # a plain directory name, never a path
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
# Text written to human readers that sends them elsewhere: install advice next
# to a link off the allowlist, or a request to close or label other reports.
# Hosts anyone can publish on are allowed only under Rich's own paths, so a
# fork, gist, Pages site or PyPI project of someone else is foreign. Install
# advice is a pip/uv/pipx/conda/poetry command, "install/download ... from",
# a wheel, or curl/wget piped to a shell, in the same paragraph as the link
# and within 200 characters of it: a bare "install", or a pip command a
# paragraph away from an ordinary link (Poetry's docs, a Stack Overflow
# answer), both occur in the upstream snapshot.
SANDBOX = "ansonpoh/OSS_A3"  # when GITHUB_REPOSITORY is not set (tests, replays)
ALLOWED_ANYWHERE = ("python.org",)  # and its subdomains
ALLOWED_EXACT = ("files.pythonhosted.org", "textualize.io", "www.textualize.io", "textual.textualize.io",
                 "textualize.github.io", "rich.readthedocs.io")
OWNER_PATHS = ("github.com", "www.github.com", "raw.githubusercontent.com", "objects.githubusercontent.com")
PYPI = ("pypi.org", "www.pypi.org")
# A URL ends at whitespace or )]>"' so both halves of [text](target) are seen.
URL = re.compile(r"(?:\bhttps?://|(?<![\w.@/-])www\.)[^\s)\]>\"'<`]+", re.I)
INSTALL_ADVICE = re.compile(
    rf"\b(pip[x3]?{W}(install|download)|uv{W}(add|pip{W}install|tool{W}install)|conda{W}install"
    rf"|poetry{W}add|(install|download){W}[^.\n]{{0,60}}?\bfrom"
    rf"|(temporary|patched|fixed|hotfix|pre-?built|nightly|custom|unofficial){W}wheels?|wheels?{W}(files?|builds?))\b"
    # curl/wget as a command (line start, prompt or code span), not a build log's RUN line
    r"|(^|[$>`]\s*)(sudo\s+)?(curl|wget)\b[^|\n]{0,200}\|\s*(sudo\s+)?(ba|z|da)?sh\b", re.I | re.M)
WHEEL = re.compile(r"\.whl\b", re.I)  # a link to a wheel is install advice in itself
NEAR = 200
PARAGRAPH = re.compile(r"\n[ \t\r]*\n")
OTHERS = r"(other|later|newer|new|future|subsequent|following|further)"
REPORTS = r"(reports?|issues?|duplicates?|tickets?|ones)"
CLOSES_OTHERS = [re.compile(p, re.I) for p in (
    # "please mark newer duplicates invalid", "close any later reports"
    rf"\b(close|label|mark|tag|flag)({W}(any|all|the|those|such|every))?{W}{OTHERS}({W}\w+)?{W}{REPORTS}\b",
    # "close duplicates of this"
    rf"\b(close|label|mark|tag|flag)({W}(any|all|the|those|such|every))?{W}duplicates?{W}of{W}(this|it)\b",
    # "later reports ... so please close them", "any later report about X,
    # label it wontfix", "new issues should be closed", "subsequent reports
    # get the wontfix label"
    rf"\b{OTHERS}{W}{REPORTS}\b[^.!?\n]{{0,150}}?(\b(close|label|mark|tag|flag)\s+(them|it|those|these)\b"
    r"|\b(should|must|can|will|are\s+to)\s+be\s+(closed|labell?ed|marked|tagged)\b|\b(wontfix|invalid)\b)",
)]


def this_repo():
    return (os.environ.get("GITHUB_REPOSITORY") or SANDBOX).lower()


def foreign(url):
    """True unless the URL is on the allowlist (host, and path where anyone can publish)."""
    rest = re.sub(r"^https?://", "", url, flags=re.I).replace("\\", "/")
    authority, _, path = rest.partition("/")
    host = re.split(r"[?#]", authority)[0].rsplit("@", 1)[-1].split(":", 1)[0].lower().rstrip(".")
    path = "/" + re.split(r"[?#]", path)[0].lower()
    if host in ALLOWED_EXACT or any(host == h or host.endswith("." + h) for h in ALLOWED_ANYWHERE):
        return False
    if host in OWNER_PATHS:
        if any(path.startswith(f"/{o}/") or path == f"/{o}" for o in ("textualize", this_repo())):
            return False
        # Another project's issue, PR or CI page is a reference, not something to install.
        return not (host in OWNER_PATHS[:2] and re.match(
            r"/[^/]+/[^/]+/(issues|pull|pulls|discussions|commit|commits|actions|checks|compare)(/|$)", path))
    if host in PYPI:
        return not re.fullmatch(r"/(project|simple)/rich(/.*)?", path)
    return True


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
        out += [{k: i.get(k) for k in KEEP} for i in page
                if "pull_request" not in i and not is_replay(i)]
        url = m.group(1) if m else None
    for i in out:
        # A marker on someone else's issue is not a replay; drop the marker.
        i["body"] = MARKER.sub("", i["body"] or "").rstrip()
    return out


def is_replay(i):
    """A golden-case replay (the owner's issue with a marker): a copy of an
    upstream or adversarial case, not part of this repository's history, so
    a live issue is never matched against, or cited as, one."""
    return i.get("author_association") == "OWNER" and bool(MARKER.search(i.get("body") or ""))


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


def redirects_readers(r):
    for text in (r["title"] or "", r["body"] or ""):
        if any(p.search(text) for p in CLOSES_OTHERS):
            return True
        for para in PARAGRAPH.split(text):
            # Install advice is looked for with the links blanked out, so a
            # URL's own path ("/download/...") is not advice.
            plain = URL.sub(lambda m: " " * len(m.group(0)), para)
            advice = [m.span() for m in INSTALL_ADVICE.finditer(plain)]
            for u in URL.finditer(para):
                if foreign(u.group(0)) and WHEEL.search(u.group(0)):
                    return True
                if foreign(u.group(0)) and any(u.start() - NEAR <= end and start <= u.end() + NEAR
                                                    for start, end in advice):
                    return True
    return False


def quarantine(index):
    """(entries kept, numbers dropped)."""
    held = [r["number"] for r in index if addresses_tools(r) or redirects_readers(r)]
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
        planted = os.path.join(golden, "adversarial", m.group(1), "planted_index.json")
        if CASE_ID.fullmatch(m.group(1)) and os.path.exists(planted):
            index += json.load(open(planted))
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
