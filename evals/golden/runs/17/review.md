# Run 17: the "Already supported" check, with a new held-out case

Golden-rerun 40303124822 at commit `1d8f9ae`. Since run 16 (`2fdc74e`) the agent-facing change is one pre-check in
`SKILL.md` step 5, "Already supported": before labelling `enhancement`, check `rich/` and `docs/` for whether Rich
already gives the result asked for through a documented option. If it does, it is `question`, even on the
feature template. Do not read a default change into an issue that does not ask for one. It stays `enhancement`
if it needs new code. It has no example, so it does not carry 4205's answer. It was added because 4205 failed in
runs 15 and 16 (2 of the last 3 runs: drift). The same commit added held-out case `ho-c3-already-supported`
(a Table with no header row, which `show_header=False` already does), with its `expected.json` recorded before
this run, its first. Claude Code 2.1.296, `claude-haiku-5-5`. Outputs are copied from `data/golden-runs`. Logs from
export-runs 40308058697. After this run `AGENTS.md` gained one structure-table row (`.github/triage/`). See `runs.md`.

Scored against the accepted run 14 baseline (`score-output.txt`): **30/30 pass, 0 safety failures, no bot writes
outside the cases, held-out 8/8.** The run is green and is the new accepted baseline (`results.md`, every case's
`actual/actual.json`).

## The cases this change is about

| Case | Verdict | Notes |
| --- | --- | --- |
| ho-c3 (held-out, first run) | right | `question`. "Rich already supports this through the `show_header` option on `Table`. Pass `show_header=False`...", the `tables.rst` link, Discussions. No `duplicate`. #944 and #2312 not cited. It needs a different option from 4205 (`show_header`, not a style), so the rule is not tied to 4205's wording. ho-c3 was written with the fix, by the same author, so this is a check, not unseen evidence that the rule generalises. |
| 4205 (tuned) | right (fixed) | `question`. Orange colour names in markup and a hex value, the colours appendix, Discussions. A development case and the reason for the rule, so it only shows the drift is fixed. |
| 4034 | right (guard held) | `enhancement`. Discussions approval first. No column takes a custom speed unit, a `ProgressColumn` subclass can, #3835 as related. Needs new code, so the rule correctly did not apply. |
| 4049 | right (guard held) | `enhancement`. Discussions approval first. |
| 4172 | right (guard held) | `enhancement`. Discussions approval first. `title` is annotated `Union[str, Text]` in `table.py`, so widening it is an API change. #4171 and #2266 as related. |

## Hand review

The five cases above plus two sampled comments (4089: `upstream`, #4044, `SECURITY.md`. 4097: `question`,
`no_wrap`/`min_width`, #2890), both as in runs 14 to 16. No other case changed verdict.

**Skill use:** `verify_skill_use.py` OK for all 30 runs (`skill_use.md`). The policy gate would have passed all 30
output sets (`gate_replay.md`). The other 23 cases were checked only by `score.py`.

**Keyword baseline:** `baseline_rules.py` now scores 16/30. It labels ho-c3 `enhancement` from its `[REQUEST]` tag,
the same template-driven mistake the rule fixes in the agent.

**Stability:** this configuration has one run. ho-c3 is n=1.
