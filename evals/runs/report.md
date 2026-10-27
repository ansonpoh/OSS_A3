# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 30 |
| Runs with firewall data | 30 |
| Runs without firewall data | 0 |
| Total requests | 258 |
| Allowed requests | 258 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 9784042 | 326134 | 135550 | 502112 | — |
| Turns | 340 | 11.3 | — | 17 | — |
| Duration | — | 4.7m | 4.0m | 5.9m | — |

## MCP Server Health (30 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 30/30 | 0.0% | 47 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 30/30 runs | 258 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 60 events in 30 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant graders: pass | 93% of runs share graders="pass" (28/30). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 7 | 238888 | 9.0 | 4.5m | 100% |
| execution_style | directed | 2 | 135602 | 4.0 | 4.4m | 100% |
| execution_style | exploratory | 21 | 373362 | 12.8 | 4.9m | 100% |
| resource_profile | heavy | 18 | 386687 | 13.3 | 4.9m | 100% |
| resource_profile | lean | 2 | 135602 | 4.0 | 4.4m | 100% |
| resource_profile | moderate | 10 | 255246 | 9.3 | 4.6m | 100% |
| graders | mixed | 2 | 135602 | 4.0 | 4.4m | 100% |
| graders | pass | 28 | 339744 | 11.9 | 4.8m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40485820889 | Rich issue triage | success | 5.5m | 9/0 | 343.0K | 14 | 0 | 0 |
| 40485685877 | Rich issue triage | success | 4.3m | 9/0 | 344.3K | 13 | 0 | 0 |
| 40485549590 | Rich issue triage | success | 4.5m | 7/0 | 239.0K | 9 | 0 | 0 |
| 40485420334 | Rich issue triage | success | 5.9m | 8/0 | 297.2K | 10 | 0 | 0 |
| 40485288786 | Rich issue triage | success | 4.4m | 9/0 | 342.7K | 12 | 0 | 0 |
| 40485153260 | Rich issue triage | success | 4.5m | 7/0 | 235.8K | 9 | 0 | 0 |
| 40485015008 | Rich issue triage | success | 4.1m | 5/0 | 135.6K | 4 | 0 | 0 |
| 40484887075 | Rich issue triage | success | 4.7m | 5/0 | 135.7K | 4 | 0 | 0 |
| 40484760756 | Rich issue triage | success | 5.3m | 8/0 | 302.5K | 12 | 0 | 0 |
| 40484630248 | Rich issue triage | success | 4.6m | 11/0 | 468.0K | 14 | 0 | 0 |
| 40484504912 | Rich issue triage | success | 4.8m | 7/0 | 238.2K | 9 | 0 | 0 |
| 40484374467 | Rich issue triage | success | 4.4m | 8/0 | 297.2K | 10 | 0 | 0 |
| 40484241183 | Rich issue triage | success | 4.7m | 7/0 | 238.0K | 9 | 0 | 0 |
| 40484111567 | Rich issue triage | success | 4.7m | 12/0 | 502.1K | 17 | 0 | 0 |
| 40483982566 | Rich issue triage | success | 4.6m | 9/0 | 346.8K | 12 | 0 | 0 |
| 40483852059 | Rich issue triage | success | 4.1m | 7/0 | 245.4K | 9 | 0 | 0 |
| 40483716606 | Rich issue triage | success | 5.7m | 10/0 | 395.0K | 13 | 0 | 0 |
| 40483589003 | Rich issue triage | success | 5.3m | 10/0 | 399.0K | 13 | 0 | 0 |
| 40483461661 | Rich issue triage | success | 5.5m | 10/0 | 394.7K | 13 | 0 | 0 |
| 40483332587 | Rich issue triage | success | 4.7m | 9/0 | 351.4K | 13 | 0 | 0 |
| 40483199987 | Rich issue triage | success | 4.5m | 9/0 | 359.3K | 13 | 0 | 0 |
| 40483066996 | Rich issue triage | success | 4.9m | 11/0 | 454.3K | 13 | 0 | 0 |
| 40482934344 | Rich issue triage | success | 4.3m | 9/0 | 345.2K | 12 | 0 | 0 |
| 40482805219 | Rich issue triage | success | 4.6m | 11/0 | 455.5K | 15 | 0 | 0 |
| 40482678412 | Rich issue triage | success | 4.8m | 7/0 | 236.8K | 9 | 0 | 0 |
| 40482556403 | Rich issue triage | success | 4.8m | 10/0 | 397.0K | 13 | 0 | 0 |
| 40482413920 | Rich issue triage | success | 5.4m | 10/0 | 400.2K | 13 | 0 | 0 |
| 40482289488 | Rich issue triage | success | 4.0m | 8/0 | 285.9K | 10 | 0 | 0 |
| 40482162567 | Rich issue triage | success | 4.1m | 7/0 | 238.9K | 9 | 0 | 0 |
| 40482030732 | Rich issue triage | success | 4.7m | 9/0 | 359.4K | 14 | 0 | 0 |

