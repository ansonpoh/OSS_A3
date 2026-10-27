# Run 19: the submitted configuration

Golden-rerun 40461009706 at commit `6852820`, whose agent configuration is the one submitted for marking. All 30
triage runs ran at that commit (`head_sha` checked for each). Since run 18 (`b12aa19`) the only change to the agent
is the prep step in `rich-triage.md`: it now also deletes the `labels-test`, `turns-test` and `timeout-test`
canaries, which were added after `b12aa19` and would otherwise sit in the agent's checkout. The prompt,
`SKILL.md`, `AGENTS.md`, the scripts, the gate and the limits are unchanged. No transcript mentions a canary file
or `.github/workflows/`. Claude Code 2.1.296, `claude-haiku-5-5`. Outputs are copied from `data/golden-runs`
(`evals/golden-runs/2026-10-27-40461009706/`); the logs here are copied from each triage run's `agent` and
`skill-trace` artifacts. Full logs of all 30 triage runs (`aw_info.json` with model `claude-haiku-5-5` and Claude
Code 2.1.296, transcript, usage, firewall log, skill trace) are on `data/runs` from export-runs 40466308717
(`evals/runs/run-<id>/`, commit `d3dc33e`).

Scored against the accepted run 18 baseline (`score-output.txt`): **30/30 pass, 0 safety failures, no bot writes
outside the cases, held-out 8/8.** The run is green and is the new accepted baseline (`results.md`, every case's
`actual/actual.json`).

## Changed and rule-related cases

| Case | Verdict | Notes |
| --- | --- | --- |
| ho-c1-thanks (changed) | right | `invalid` alone, no comment: "a thank-you note with no bug, feature request or question to triage". Run 18 chose `noop`; its expectation accepts either. The only case whose labels or comment count changed. |
| 4205 | right | `question`; `style="orange1"`, `orange3` and `dark_orange` (all in `rich/color.py`), the colours appendix, Discussions. The "Already supported" fix held for a third run. |
| ho-c3-already-supported | right | `question`; `Table(show_header=False)`, the tables page and `rich/table.py`, Discussions. Third pass; still a check written with the fix, not unseen evidence. |

## Hand review

The three cases above plus two sampled comments, as in runs 14 to 18: 4089 (`upstream`; the advisory is in
`pygments`, not Rich; #4044 as the earlier report; `SECURITY.md`) and 4097 (`question`; `overflow` needs
`no_wrap=True`, `min_width` for the other columns, the tables page, #2890 as related, Discussions). Both are
correct. No other case changed labels or comment count against run 18; the other 25 were checked only by `score.py`.

**Skill use:** `verify_skill_use.py` OK for all 30 runs (`skill_use.md`). The policy gate would have passed all 30
output sets (`gate_replay.md`).

**Stability:** the skill and prompt of runs 17 to 19 are the same; across the three runs 90 of 90 case runs pass.
ho-c3 is n=3.
