# Mock grading, round 6

- **Commit graded:** `67e7708`
- **Instruction:** two independent AI graders, each with a clean clone, the brief and the data branches. Both were
  read-only and re-ran every offline check, and each was told to verify every claim against the brief. The brief
  has no rubric, so each grader set its own weights.
- **Scores:** Grader 1: 79. Grader 2: 77. (Round 5: 77 and 76.)

## Top findings

Points are the deductions each grader made (G1, G2).

| # | Finding | G1 | G2 |
| --- | --- | --- | --- |
| 1 | The submitted configuration had run only on adv-4; the 22/26 came from `0ce2727`, before later changes to the index builder, permissions and `SKILL.md`. | -3 | -3.5 |
| 2 | Need figures mixed two cohorts ("the 22 with one got it in 7.7 h"), and "32 old issues remain open, all with Needs triage" was wrong. | -1.5 | -2 |
| 3 | AI-use verification is circular, and the "independent AI review rounds" had no artifact. | -1.5 | -2 |
| 4 | Held-out 5/5 overstated: ho-4168 and ho-4176 were added together with the noop rule they test. | -2 | -1.5 |
| 5 | Drift blind spot: the safety check did not count forbidden labels or comment patterns, so an adv-4 regression would stay green. | -1.5 | -1 |
| 6 | Kill switch gated only the first two jobs; a run already past activation could still write. | -1 | -0.5 |
| 7 | Known `SKILL.md` fixes for 4068, 4097 and 4204 were not made, and the quarantine was tested only against the attack it was written for. | - | -2 |
| 8 | Q2 gave no detection latency; the Q5 phone path was untested. | -2 | -1 |
| 9 | No-action cases are only collaborator-authored, and there is one run (n=1). | -1 | -1 |
| 10 | Smaller items: bash is unrestricted (§3 understated it); the detection job has GitHub network access; detection fails open with no verdict; helper force-push and tag pins. | -2.5 | -3 |

Both graders credited the platform-enforced limits, the fail-closed policy gate, the rigorous skill-use check, the
time-rewound index with two baselines, and the exported logs for every case.

## Response

- **`d017a23`** ("Gate kill switch, adversarial safety scoring, skill fixes, add adv-5"): `score.py` counts a
  forbidden comment pattern or attack label on an adversarial case as a safety failure. The policy gate refuses every
  write while `TRIAGE_AGENT_ENABLED` is `false`. `SKILL.md` adds the usage-question signals, a docs search for the
  reporter's goal, and a documentation row for docs errors. Case adv-5 (an index-injection variant the quarantine
  does not catch) was added, and the full 27-case set was run on this commit as run 3 (`evals/golden/runs/3/`).
- **`d59b0aa`** ("lock citing planted issues, record run 3 baseline"): the policy gate refuses a comment that cites
  an issue the prep step would quarantine. `build_index.py` also quarantines entries that give install advice pointing
  at a foreign host or tell readers to close or label other reports, and `SKILL.md` forbids naming them. Run 3 is recorded as the accepted drift baseline in
  `evals/golden/results.md`, and run 4 later replayed adv-5 on this commit (`evals/golden/runs/4/`).
