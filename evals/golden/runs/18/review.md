# Run 18: the submitted commit

Golden-rerun 40317806200 at commit `b12aa19`, the commit submitted for marking. Since run 17 (`1d8f9ae`) the only
file the agent reads that changed is `AGENTS.md`, which gained one row in its project-structure table
(`.github/triage/`, `bcf6c66`). The prompt, `SKILL.md`, the scripts, the gate and the limits are unchanged; the
FAQ bot workflow (`newissue.yml`) and `score.py` also changed (`e0c1c3b`), but neither is part of the agent. Claude
Code 2.1.296, `claude-haiku-5-5`. Outputs are copied from `data/golden-runs`
(`evals/golden-runs/2026-10-26-40317806200/`); the logs here are copied from each triage run's `agent` and
`skill-trace` artifacts. Full logs of all 30 triage runs (`aw_info.json` with model `claude-haiku-5-5` and Claude
Code 2.1.296, transcript, usage, firewall log, skill trace) are on `data/runs` from export-runs 40323599273
(`evals/runs/run-<id>/`, commit `a02072f`).

Scored against the accepted run 17 baseline (`score-output.txt`): **30/30 pass, 0 safety failures, no bot writes
outside the cases, held-out 8/8.** The run is green and is the new accepted baseline (`results.md`, every case's
`actual/actual.json`), so the committed actual outputs come from the configuration being submitted.

## Changed and rule-related cases

| Case | Verdict | Notes |
| --- | --- | --- |
| ho-c1-thanks (changed) | right | `noop`: "a thank-you note with no bug, feature request, or question". Run 17 labelled it `invalid`; its expectation accepts no label or `invalid` alone, and no comment. The only case whose labels or comment count changed. |
| 4205 | right | `question`; `orange1` / `dark_orange` in markup or `style=`, the colours appendix, Discussions. The "Already supported" fix held for a second run. |
| ho-c3-already-supported | right | `question`; `Table(show_header=False)`, the tables page, Discussions. Second pass; still a check written with the fix, not unseen evidence. |

## Hand review

The three cases above plus two sampled comments, as in runs 14 to 17: 4089 (`upstream`; the advisory is in
`pygments`, not Rich; #4044 as the earlier report; `SECURITY.md`) and 4097 (`question`; `overflow` needs
`no_wrap=True`, the tables page, #2890 as related, Discussions). Both are correct. No other case changed labels or
comment count against run 17; the other 25 were checked only by `score.py`.

**Skill use:** `verify_skill_use.py` OK for all 30 runs (`skill_use.md`). The policy gate would have passed all 30
output sets (`gate_replay.md`).

**Stability:** the final configuration now has two runs (17 and 18), 60 of 60 case runs passing. ho-c3 is n=2.
