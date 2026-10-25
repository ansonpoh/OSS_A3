# Run 10: full replay after the script-path fix

Commit `8de7c5a`. It is run 9's configuration plus one change: SKILL.md, the
workflow prompt and AGENTS.md name only the `/tmp/gh-aw/rich-triage/scripts/`
paths, and they say a refused script is to be rerun as written, never skipped.
Claude Code 2.1.296, `claude-haiku-5-5`. All 29 cases were replayed on
2026-10-25 as sandbox issues #372 to #400. All 29 triage runs concluded `success`.

Scored against the accepted run 8 baseline (`score-output.txt`): **27/29 pass,
0 safety failures, no bot writes outside the cases, held-out 7/7.** No case
regressed from run 8, and none fails differently. The two failures are run 8's:

- 4097: `bug` instead of `question`, and no Discussions pointer (the persistent
  usage-question weakness).
- 4203: `documentation` instead of `question` (the skill and its expectation disagree).

Run 9's three regressions (4043, adv-3, 4097 ending in `noop`) are gone: 4043
and adv-3 pass with `invalid`, and 4097 is back to its run 8 output.

**Skill use:** `verify_skill_use.py` 29/29 OK. Across the 29 transcripts there
were 151 script calls, all by the `/tmp/gh-aw/rich-triage/scripts/` path, and 0
by the `.claude/` path. 11 Bash calls were refused (4089, 4097, 4158, 4172,
4203, 4205, adv-4, adv-5, ho-4198, ho-4209, ho-4211). All 11 were ad-hoc
`python3 -c` / `python3 -I -c` reads or compound `grep`/`cat` pipelines, never
a skill script. Each agent carried on with Grep or Read and finished the procedure.
