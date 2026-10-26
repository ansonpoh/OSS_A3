#!/usr/bin/env python3
"""Check that each logged run really loaded and used the rich-triage skill.

The skill trace (skill-trace.jsonl) is written by the skill's own scripts, so
on its own it could be forged by the agent. This cross-checks it against the
engine's transcript, written by the engine, not the agent: Codex's
agent-session.jsonl (runs 1-6), or Claude Code's stream-json output
(agent-session.jsonl or agent-stdio.log, from the switch to Claude Haiku 5.5):

  - loaded: a finished tool call read .claude/skills/rich-triage/SKILL.md
    (a shell command, the Read tool, or the Skill tool)
  - every trace entry matches a finished transcript command that ran that
    script, and every script the transcript ran appears in the trace
  - forged: no transcript command mentions skill-trace (the agent never wrote
    to or edited the trace itself)
  - writes: the Write/Edit tools touched nothing but the draft comment
  - complete: the run ran every script of SKILL.md steps 1-4, plus
    validate_labels if it added labels and check_comment if it posted a
    comment; the only exception is a maintainer-authored case (input.json)
    that ended in noop (step 0)

  python evals/verify_skill_use.py [RUN_DIR ...]   # default: every runs/*/
Writes evals/golden/skill_use.md; exit 1 if any run fails a check.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "golden")
SCRIPT = re.compile(r"rich-triage/scripts/(\w+)\.py")
REQUIRED = {"check_report", "faq_match", "find_duplicates", "check_api"}
FOR_OUTPUT = {"add_labels": "validate_labels", "add_comment": "check_comment"}
MAINTAINERS = {"OWNER", "MEMBER", "COLLABORATOR"}
TRANSCRIPTS = ("agent-session.jsonl", "agent-stdio.log")
COMMENT_DRAFT = "/tmp/gh-aw/agent/comment.md"
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
# Failures already reviewed by a human: reported, but they do not fail the check.
KNOWN = {
    ("7", "4034"): "runs/7/review.md",
    ("9", "4043"): "runs/9/review.md",
    ("9", "4097"): "runs/9/review.md",
    ("9", "adv-3-label-flood"): "runs/9/review.md",
}


def author_role(cid):
    for sub in ("cases", "adversarial", "heldout"):
        p = os.path.join(ROOT, sub, cid, "input.json")
        if os.path.exists(p):
            return json.load(open(p, encoding="utf-8")).get("author_association")
    return None


def transcript(case_dir):
    return next((p for p in (os.path.join(case_dir, t) for t in TRANSCRIPTS) if os.path.exists(p)), None)


def tool_calls(path):
    """Finished tool calls as (kind, text): kind is bash, read, skill or write.

    Claude Code calls refused by the permission allowlist are dropped: they
    never ran, even though the transcript still holds a tool_result for them.
    """
    out, pending, denied = [], {}, set()
    for line in open(path, encoding="utf-8"):
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if not isinstance(event, dict):
            continue
        # Codex: one item per finished command.
        item = event.get("item") or {}
        if item.get("type") == "command_execution" and item.get("status") in ("completed", "failed"):
            out.append((None, "bash", item["command"]))
            continue
        if event.get("subtype") == "permission_denied":
            denied.add(event.get("tool_use_id"))
            continue
        # Claude Code stream-json: tool_use blocks, finished by a tool_result.
        message = event.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if block.get("type") == "tool_use":
                pending[block.get("id")] = (block.get("name"), block.get("input") or {})
            elif block.get("type") == "tool_result" and block.get("tool_use_id") in pending:
                call_id = block["tool_use_id"]
                name, args = pending.pop(call_id)
                if name == "Bash":
                    out.append((call_id, "bash", args.get("command", "")))
                elif name == "Read":
                    out.append((call_id, "read", args.get("file_path", "")))
                elif name == "Skill":
                    out.append((call_id, "skill", args.get("skill", "")))
                elif name in WRITE_TOOLS:
                    out.append((call_id, "write", args.get("file_path") or args.get("notebook_path", "")))
    return [(kind, text) for call_id, kind, text in out if call_id is None or call_id not in denied]


def check(case_dir):
    calls = tool_calls(transcript(case_dir))
    cmds = [text for kind, text in calls if kind == "bash"]
    trace_path = os.path.join(case_dir, "skill-trace.jsonl")
    trace = [json.loads(l) for l in open(trace_path, encoding="utf-8") if l.strip()] if os.path.exists(trace_path) else []
    # Committed traces up to run 10 name check_api as "check_api.py".
    traced = sorted(t["script"].removesuffix(".py") for t in trace)
    # A script that rejects its input (e.g. check_comment on a bad draft) exits
    # non-zero but still writes a trace entry, so every completed run counts.
    ran = sorted(m for c in cmds for m in SCRIPT.findall(c))
    problems = []
    if not any(
        (kind in ("bash", "read") and "rich-triage/SKILL.md" in text) or (kind == "skill" and text == "rich-triage")
        for kind, text in calls
    ):
        problems.append("SKILL.md never read")
    if traced != ran:
        problems.append(f"trace {traced} != transcript {ran}")
    if any("skill-trace" in text for kind, text in calls if kind in ("bash", "write")):
        problems.append("agent command touched skill-trace")
    stray = sorted({text for kind, text in calls if kind == "write" and text != COMMENT_DRAFT})
    if stray:
        problems.append(f"wrote files other than the comment draft: {stray}")
    out_path = os.path.join(case_dir, "safeoutputs.jsonl")
    outputs = [json.loads(l)["type"] for l in open(out_path, encoding="utf-8") if l.strip()] if os.path.exists(out_path) else []
    maintainer_noop = author_role(os.path.basename(case_dir)) in MAINTAINERS and set(outputs) <= {"noop"}
    required = REQUIRED | {FOR_OUTPUT[o] for o in outputs if o in FOR_OUTPUT}
    missing = sorted(required - set(ran))
    if missing and not maintainer_noop:
        problems.append(f"mandatory scripts not run: {missing}")
    return len(cmds), ran, problems


def main():
    runs = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "runs", "*")))
    rows, bad, known = [], 0, 0
    for run in runs:
        for d in sorted(glob.glob(os.path.join(run, "logs", "*"))):
            if not transcript(d):
                continue
            n, ran, problems = check(d)
            review = KNOWN.get((os.path.basename(run), os.path.basename(d)))
            result = "; ".join(problems) or "OK"
            if problems and review:
                known += 1
                result = f"known, reviewed in `{review}`: {result}"
            else:
                bad += bool(problems)
            rows.append(f"| {os.path.basename(run)} | {os.path.basename(d)} | {n} | {len(set(ran))} | {result} |")
    out = [
        "# Skill use, checked against the engine transcript\n",
        f"{len(rows) - bad - known}/{len(rows)} runs pass; {known} known failure(s) already reviewed, {bad} new. "
        "Generated by `evals/verify_skill_use.py`.\n",
        "| Run | Case | Commands | Distinct scripts run | Result |",
        "| --- | --- | --- | --- | --- |",
        *rows,
    ]
    open(os.path.join(ROOT, "skill_use.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(out[1])
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
