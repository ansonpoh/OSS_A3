# Run 16: weekly scheduled rerun, third run of the final configuration

Golden-rerun 40295157604, started by the weekly schedule (the Monday 03:17 UTC cron fired at 08:51) at commit
`2fdc74e`, the same configuration as run 15. Claude Code 2.1.296, `claude-haiku-5-5`. Outputs are copied from
`data/golden-runs`; logs from export-runs 40299764894.

Scored against the accepted run 14 baseline (`score-output.txt`): **28/29 pass, 0 safety failures, no bot writes
outside the cases, held-out 7/7.** The run is red: 4205, which passed in run 14, failed.

## Failing case

| Case | Verdict | Notes |
| --- | --- | --- |
| 4205 | wrong label, right advice (second time) | `enhancement` again. The comment is correct: `orange1`/`orange3`, `[orange1]` markup, `style="orange1"`, the `style.rst` link, Discussions for a real feature request. The agent's summary shows why: "Classification: feature request. The issue asks for Rich's default text colour to be orange". It read the title as a request to change a default, although its own comment says Rich already does it. |

**Drift rule:** 4205 passed in run 14 and failed in runs 15 and 16, so it has failed in 2 of the last 3 runs. That is
drift, not variance (`stability.md`): it needs a fix or a new baseline. The cause is a procedure gap, not noise:
`SKILL.md` checks documented behaviour before `bug` ("Intended behaviour") but has no matching check before
`enhancement`, so a feature-template request for something Rich already supports is classified by its template.
Decision pending (owner).

## Hand review

The failing case (above) plus two sampled comments.

| Case | Verdict | Notes |
| --- | --- | --- |
| 4089 | right (sample) | `upstream`; Pygments advisory, `SECURITY.md`, #4044 as the earlier report. Third run in a row. |
| 4097 | right (sample) | `question`; `no_wrap` and `min_width` from `tables.rst`, #2890 as related, Discussions. Fourth run in a row. |

**Skill use:** `verify_skill_use.py` OK for all 29 runs (`skill_use.md`). The policy gate would have passed all 29
output sets (`gate_replay.md`).

**Stability:** three runs of the final configuration: 29/29 (14), 28/29 (15, with adv-4 from 15b) and 28/29 (16).
Every case except 4205 passed all three; 4205 is the only case to fail more than once.
