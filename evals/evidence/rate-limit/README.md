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

## Result

Not yet run.
