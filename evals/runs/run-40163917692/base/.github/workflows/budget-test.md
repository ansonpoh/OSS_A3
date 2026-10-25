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
max-daily-ai-credits: 1    # so a second run within 24 h is skipped

network: {}

tools:
  bash: true
  edit: false
  github: false

safe-outputs:
  # The canary only calls noop. Without a non-builtin output gh-aw would
  # auto-inject create-issue, so allow at most one comment on the test issue.
  add-comment:
    max: 1
    target: triggering
    pull-requests: false
    discussions: false
  noop:
    report-as-issue: false
  report-failure-as-issue: false
  report-incomplete:
    create-issue: false
  report-missing-tool:
    create-issue: false
  report-missing-data:
    create-issue: false
  # Same detection settings as rich-triage.md: no "[aw] Detection Runs" issue.
  threat-detection:
    continue-on-error: false
    report-as-issue: false
---

# Package summary

Write a reference summary of the `rich` package. List every Python file under
`rich/`, then read each one in full in chunks of at most 150 lines
(`sed -n '1,150p' FILE`, then `sed -n '151,300p' FILE`, and so on), one chunk
per command, until you reach the end of the file. After each file, write a
three-sentence summary of what it does. Cover every file and skip none. When
all files are covered, call `noop` with the message "summaries finished".
