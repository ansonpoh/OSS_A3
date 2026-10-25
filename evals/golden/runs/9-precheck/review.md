# Run 9 precheck: one-case check of the post-review hardening

Commit `c889310` (six-script Bash allowlist run from a read-only copy in
`/tmp/gh-aw/rich-triage/scripts`, read-only `rich/`, tighter link checks and
policy gate). Claude Code 2.1.296, `claude-haiku-5-5`. One paid case, 4034,
replayed as sandbox issue #342, run
[40193291792](https://github.com/ansonpoh/OSS_A3/actions/runs/40193291792):
every job succeeded, 1.49 AI credits.

- **Verdict:** PASS (`score-output.txt`): `enhancement` and one comment pointing
  to Discussions, `TaskProgressColumn` (`show_speed`), `TransferSpeedColumn` and
  subclassing `ProgressColumn`; it cites #3835 as related. No bot writes outside the case.
- **Skill use:** `verify_skill_use.py` OK. All six scripts ran from
  `/tmp/gh-aw/rich-triage/scripts/` (`logs/4034/skill-trace.jsonl` matches the
  transcript). The only file written was `/tmp/gh-aw/agent/comment.md`.
- **Read-only copy:** the agent's own `ls -la` shows `dr-xr-xr-x` on the
  directory and `-r--r--r--` on every script, owned by `runner` (non-root).
- **Allowlist:** one ad-hoc `python3 -c` to read the index was refused
  ("Permission to use Bash has been denied"). The agent carried on with Grep and
  finished the procedure; it did not mistake the refusal for Bash being off.

Not covered: one case says nothing about the other 28 under this commit. The
gate's live earlier-issue rule was not exercised (replays use the snapshot path).
