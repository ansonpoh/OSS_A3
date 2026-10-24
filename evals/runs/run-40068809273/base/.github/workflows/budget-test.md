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
max-turns: 25
max-ai-credits: 1          # the per-run cap under test (a triage uses about 0.7)
max-daily-ai-credits: 1    # so a second run within 24 h is skipped

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

This is an authorised test of this repository's budget limits. Read every
Python file under `rich/` in full, one file per command, and after each file
write a three-sentence summary of it. Continue until you have covered every
file, then call `noop` with the message "budget test finished".
