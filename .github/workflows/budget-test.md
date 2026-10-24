---
name: Budget cap test
description: Canary that deliberately uses more AI credits than its 1-credit budget, to show the per-run cap stops a run and the daily cap skips the next. Run by adding the budget-test label to a test issue.
on:
  issues:
    types: [labeled]
    names: [budget-test]
  roles: [admin]

permissions:
  contents: read

engine:
  id: codex
  version: "0.163.0"
  model: gpt-6-luna-2026-09-22

strict: true
timeout-minutes: 10
max-turns: 80              # high, so the credit cap is what stops the run
max-ai-credits: 1          # the per-run cap under test (a triage uses about 0.7)
max-daily-ai-credits: 3    # raised for the per-run cap retest; set back to 1 afterwards

network: {}

tools:
  bash: true
  edit: false
  github: false

safe-outputs:
  noop:
    report-as-issue: false
  report-failure-as-issue: false
  report-incomplete:
    create-issue: false
---

# Budget cap test

This is an authorised test of this repository's budget limits. List every
Python file under `rich/`, then read each one in full in chunks of at most
150 lines (`sed -n '1,150p' FILE`, then `sed -n '151,300p' FILE`, and so on),
one chunk per command, until you reach the end of the file. After each file,
write a three-sentence summary of it. Do not stop early or skip files:
continue until you have covered every file, then call `noop` with the
message "budget test finished".
