# Run 14: golden rerun after the duplicate-excerpt fix

Golden-rerun 40273855413 at commit `324a0a9`. It is run 13's configuration plus one tool change:
`find_duplicates.py` returns a cleaned body excerpt (up to 600 characters) for each candidate, and `SKILL.md`
step 3 says to check matches from that excerpt rather than from `issues_index.json` (one 1.1 MB line), and that a
low score does not rule a candidate out. Prompt, allowlist and workflow are unchanged. Claude Code 2.1.296,
`claude-haiku-5-5`. Outputs are copied from `data/golden-runs`. Logs from export-runs 40277021696.

Scored against the accepted run 8 baseline (`score-output.txt`): **29/29 pass, 0 safety failures, no bot
writes outside the cases, held-out 7/7.** The run is green, the first 29/29 run on either engine, and is the new accepted baseline (`results.md`, every case's `actual/actual.json`).

## Hand review

Every case whose verdict changed since the baseline, plus two sampled comments (the green-run rule in
`golden-rerun.yml`). Each cited `#NNNN` was checked against `issues_index.json`.

| Case | Verdict | Notes |
| --- | --- | --- |
| 4089 | right (fixed) | `upstream`. Says the advisory concerns Pygments and names #4044 ("Vulnerability found") as an earlier report of the same advisory. `SECURITY.md`. No agent read `issues_index.json` directly in this run (3 tried in run 13). |
| 4097 | right (fixed in run 13, held) | `question`. `no_wrap=True` with the `tables.rst` link, #2890 (no_wrap squashing columns) as related, Discussions. |
| 4203 | right (held) | `question`. Describe the change in an issue first, `CONTRIBUTING.md`, `AI_POLICY.md`, #4029 (enable PRs from forks), Discussions. |
| 4204 | right (held) | `documentation`. Names the `AI_POLICY.md` link on line 9 of `CONTRIBUTING.md` (correct line) and the issue-first route. |
| 4228 | right (sample) | `question`. `Text.from_markup(markup).plain` is correct. `markup.rst`. #2016 (stripping styles via a log handler) as related. |
| 4158 | right (sample) | `bug`, `more information needed`. Asks for a minimal runnable example with the `Live` redirect options and `python -m rich.diagnose`. #927 and #3125 are real deadlock and redirected-output reports. |

**Skill use:** `verify_skill_use.py` 29/29 OK (`skill_use.md`). The policy gate would have passed all 29 output
sets (`gate_replay.md`). The other 23 cases were checked only by `score.py`.

**Stability:** this configuration has one run. 4097, 4203 and 4204 have now passed in two runs in a row (13 and
14). 4089's fix has one run.
