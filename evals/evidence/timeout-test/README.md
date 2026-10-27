# Timeout test (`timeout-minutes`)

`rich-triage.md` sets `timeout-minutes: 10`, which gh-aw applies to the agent's engine step. `timeout-test.md` uses
it at 1 (as `budget-test` tests the credit caps at 1), with the triage turn (25) and credit (5) caps so that only
the timeout can stop it, and asks for five `sleep 50` commands (about 250 s), then `noop`.

- `expected.json`: written and committed (`db8855d`) before the run.
- `issue-27-before.json`, `issue-27-after.json`: labels and comments on #27.
- `timeout-test-run-40457456919.json`: jobs and timings; `agent-stop-40457456919.log`: the start and stop lines.

## Result: PASS

Run 40457456919: the agent started one `sleep 50`. At 05:51:31Z gh-aw logged "Agent command timed out after 1
minutes, stopping container", and at 05:51:33Z Actions stopped the step ("has timed out after 1 minutes"). No
retry; the agent job and the run concluded failure. `noop` was never called; safe_outputs processed only gh-aw's
`report_incomplete` signal, which creates no issue. #27 gained only the owner's `timeout-test` trigger label.

Not exercised: the job-level timeouts (60 and 45 minutes in the triage lock file).
