# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 29 |
| Runs with firewall data | 29 |
| Runs without firewall data | 0 |
| Total requests | 292 |
| Allowed requests | 292 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 11535128 | 397763 | 134436 | 829363 | ⚠ #40267101086, #40266935279 |
| Turns | 391 | 13.5 | — | 23 | — |
| Duration | — | 4.3m | 3.6m | 5.4m | — |

## MCP Server Health (29 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 29/29 | 0.0% | 44 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 29/29 runs | 292 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 58 events in 29 runs. (plan=1 finish=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant graders: pass | 93% of runs share graders="pass" (27/29). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 7 | 234064 | 9.0 | 4.0m | 100% |
| execution_style | directed | 2 | 134441 | 4.0 | 3.7m | 100% |
| execution_style | exploratory | 20 | 481389 | 16.0 | 4.5m | 100% |
| resource_profile | heavy | 18 | 502634 | 16.7 | 4.5m | 100% |
| resource_profile | lean | 2 | 134441 | 4.0 | 3.7m | 100% |
| resource_profile | moderate | 9 | 246536 | 9.2 | 4.1m | 100% |
| graders | mixed | 2 | 134441 | 4.0 | 3.7m | 100% |
| graders | pass | 27 | 417268 | 14.2 | 4.4m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40268691299 | Rich issue triage | success | 4.4m | 9/0 | 343.5K | 14 | 0 | 0 |
| 40268604271 | Rich issue triage | success | 3.6m | 7/0 | 234.2K | 9 | 0 | 0 |
| 40268512013 | Rich issue triage | success | 4.2m | 8/0 | 290.7K | 10 | 0 | 0 |
| 40268423728 | Rich issue triage | success | 4.3m | 14/0 | 590.1K | 18 | 0 | 0 |
| 40268332858 | Rich issue triage | success | 4.0m | 9/0 | 338.8K | 12 | 0 | 0 |
| 40268243688 | Rich issue triage | success | 3.7m | 5/0 | 134.4K | 4 | 0 | 0 |
| 40268155900 | Rich issue triage | success | 3.7m | 5/0 | 134.4K | 4 | 0 | 0 |
| 40268060688 | Rich issue triage | success | 4.4m | 11/0 | 445.8K | 15 | 0 | 0 |
| 40267974705 | Rich issue triage | success | 4.4m | 12/0 | 508.2K | 17 | 0 | 0 |
| 40267887333 | Rich issue triage | success | 4.0m | 7/0 | 233.3K | 9 | 0 | 0 |
| 40267798686 | Rich issue triage | success | 4.0m | 7/0 | 237.0K | 9 | 0 | 0 |
| 40267710755 | Rich issue triage | success | 4.0m | 7/0 | 234.1K | 9 | 0 | 0 |
| 40267618421 | Rich issue triage | success | 4.5m | 11/0 | 451.2K | 17 | 0 | 0 |
| 40267531791 | Rich issue triage | success | 4.2m | 8/0 | 288.9K | 13 | 0 | 0 |
| 40267446242 | Rich issue triage | success | 4.4m | 8/0 | 289.6K | 10 | 0 | 0 |
| 40267360031 | Rich issue triage | success | 4.5m | 13/0 | 570.3K | 19 | 0 | 0 |
| 40267274453 | Rich issue triage | success | 4.5m | 10/0 | 401.2K | 14 | 0 | 0 |
| 40267187690 | Rich issue triage | success | 4.7m | 13/0 | 545.1K | 18 | 0 | 0 |
| 40267101086 | Rich issue triage | success | 5.4m | 19/0 | 813.0K ⚠ | 23 | 0 | 0 |
| 40267016666 | Rich issue triage | success | 4.4m | 16/0 | 685.8K | 20 | 0 | 0 |
| 40266935279 | Rich issue triage | success | 4.5m | 17/0 | 829.4K ⚠ | 19 | 0 | 0 |
| 40266847991 | Rich issue triage | success | 5.1m | 15/0 | 643.8K | 18 | 0 | 0 |
| 40266757681 | Rich issue triage | success | 4.8m | 10/0 | 399.9K | 16 | 0 | 0 |
| 40266680353 | Rich issue triage | success | 4.3m | 7/0 | 233.8K | 9 | 0 | 0 |
| 40266600937 | Rich issue triage | success | 4.6m | 9/0 | 338.6K | 15 | 0 | 0 |
| 40266520015 | Rich issue triage | success | 4.6m | 9/0 | 339.9K | 13 | 0 | 0 |
| 40266436945 | Rich issue triage | success | 4.2m | 7/0 | 232.4K | 9 | 0 | 0 |
| 40266351619 | Rich issue triage | success | 3.9m | 7/0 | 233.8K | 9 | 0 | 0 |
| 40266270699 | Rich issue triage | success | 4.4m | 12/0 | 514.0K | 19 | 0 | 0 |

