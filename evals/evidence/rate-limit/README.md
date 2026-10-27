# Per-author rate limit test

`rich-triage.md` allows 3 triage runs per issue author per 60 minutes (`user-rate-limit`). gh-aw compiles this
into the `check_rate_limit` step of the `pre_activation` job; when it fails, `activated` is false and every later
job is skipped. Authors with `admin`, `maintain` or `write` roles are exempt, so the test uses the second,
roleless account from the live run (`a-p-j-e`, see `../live-run/`).

- `issue-1.md` to `issue-4.md`: four short usage questions, used only to trigger runs (triage quality not scored).
- `expected.json`: the expected outcome for each issue, written before any issue was opened.

## Steps (second account `a-p-j-e`)

1. Check that no issue has been opened from this account in the last 60 minutes.
2. New issue → "Open a blank issue". Copy the title and body from `issue-1.md`. Submit and note the time.
3. Wait about 1 minute. (Issues seconds apart used up the API quota of gh-aw's daily-credit scan, which then fails
   closed; that would hide the rate-limit result.)
4. Repeat for `issue-2.md`, `issue-3.md` and `issue-4.md`, about 1 minute apart. All four within 60 minutes.
5. Do not edit or comment on the issues. Send the four issue numbers to the owner.

Optional controls:

6. Owner account (`ansonpoh`), right after issue 4: open one blank issue reusing `issue-4.md`. It should run
   (admin is exempt).
7. `a-p-j-e`, more than 60 minutes after issue 1: open a fifth issue reusing `issue-1.md` with " (2)" added to the
   title. It should run again.

## Evidence (owner)

For each issue: the run ID, `gh run view RUN_ID --json jobs,conclusion,createdAt,event` saved as
`rate-limit-run-RUN_ID.json`, the `check_rate_limit` log lines (`Total recent runs in last 60 minutes: N`) and the
issue's labels and comments with their authors. `result.json` compares these with `expected.json`.

## Result: PASS

`expected.json` was committed in `9e54d4d` and pushed at 02:08:05Z, before issue 1. Issues #637 to #640 were
opened by `a-p-j-e` (association `NONE`) on 2026-10-27 between 02:10:08Z and 02:13:11Z; #641 by the owner at
02:13:41Z. The daily guardrail read 231.60/600, so it did not interfere.

| Issue | Run | Rate-limit log | Jobs | Bot writes |
| --- | --- | --- | --- | --- |
| #637 | 40436858595 | 0 recent runs, passed | all six success | `question`, one comment |
| #638 | 40436963703 | 1 recent run, passed | all six success | `question`, one comment |
| #639 | 40437060408 | 2 recent runs, passed | all six success | `question`, one comment |
| #640 | 40437155990 | 3 recent runs, **exceeded** | only pre_activation ran | none (FAQtory comment only) |
| #641 (owner) | 40437204536 | ignored role `admin`, check skipped | all six success | none: agent `noop` (owner-authored) |

Agent credits for the three triaged issues: 1.23, 0.75 and 0.60; the skipped run used none. Every check in
`expected.json` passes (`result.json`).

One finding: on a limit hit gh-aw also tries to cancel the run, which fails (`Resource not accessible by
integration`) because `pre_activation` has only `actions: read`. The skip does not depend on it (`activated` is
false), but the run shows as a success with skipped jobs rather than as cancelled.

Window reset (`expected-window-reset.json`): #643 from `a-p-j-e` at 04:11:04Z, about two hours after #637, logged 0
recent runs and was triaged (run 40448328239: `duplicate` and `question`, one comment naming #637).

Skipped runs count: per gh-aw v0.93.0's `check_rate_limit.cjs` (read, not observed), only cancelled runs and runs
under 15 s are left out. #640's run lasted 34 s and was not cancelled, so a blocked author's runs keep the window full.

Files: `rate-limit-run-RUN_ID.json` (jobs and timings), `pre_activation-RUN_ID.log` (the rate-limit step's output).
