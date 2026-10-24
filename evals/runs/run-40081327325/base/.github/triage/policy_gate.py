#!/usr/bin/env python3
"""Deterministic policy gate, run in the threat-detection job before any write.

Re-checks every output the agent proposed with the same code the skill tells
the agent to run, so these rules are enforced rather than only instructed:

- labels: allowlist, at most 3, one type label, `invalid` alone, and a
  `duplicate` label only with a comment naming the earlier issue as #NNNN;
- comments: at most 1, and `check_comment.py` must pass (links only to Rich
  files on master, never an issue/PR/discussion URL; code parses; footer);
- an issue opened by a maintainer (OWNER, MEMBER or COLLABORATOR, after the
  replay marker restores the filed role) gets no label and no comment.

Any violation, or a missing agent output file, exits 1: the detection job
fails, and gh-aw's safe_outputs job (which needs detection to succeed) writes
nothing.

  python policy_gate.py AGENT_OUTPUT_JSON GITHUB_EVENT_JSON
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, "..", "..", ".claude", "skills", "rich-triage", "scripts")
sys.path.insert(0, SCRIPTS)
os.environ.setdefault("RICH_TRIAGE_TRACE", os.devnull)

import check_comment  # noqa: E402
import validate_labels  # noqa: E402

MAINTAINERS = {"OWNER", "MEMBER", "COLLABORATOR"}
MARKER = re.compile(r"<!-- golden-case: (\S+) filed: (\S+) as: (\S+) -->")


def filed_role(issue):
    """The author role as filed (the triage prep step applies the same rule)."""
    assoc = issue.get("author_association")
    m = MARKER.search(issue.get("body") or "")
    if m and assoc == "OWNER":
        return m.group(3)
    return assoc


def gate(items, issue):
    problems = []
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
    print(json.dumps({"ok": not problems, "items": len(items), "problems": problems}, indent=2))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
