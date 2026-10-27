# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 30 |
| Runs with firewall data | 30 |
| Runs without firewall data | 0 |
| Total requests | 265 |
| Allowed requests | 265 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 10197894 | 339929 | 135446 | 629732 | — |
| Turns | 347 | 11.6 | — | 20 | — |
| Duration | — | 4.5m | 3.9m | 6.9m | — |

## MCP Server Health (30 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 30/30 | 0.0% | 47 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 30/30 runs | 265 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 60 events in 30 runs. (plan=1 finish=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant graders: pass | 93% of runs share graders="pass" (28/30). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 6 | 237357 | 8.5 | 4.3m | 100% |
| execution_style | directed | 2 | 135546 | 4.0 | 4.4m | 100% |
| execution_style | exploratory | 22 | 386484 | 13.1 | 4.6m | 100% |
| resource_profile | heavy | 17 | 412987 | 13.9 | 4.6m | 100% |
| resource_profile | lean | 2 | 135546 | 4.0 | 4.4m | 100% |
| resource_profile | moderate | 11 | 264183 | 9.3 | 4.3m | 100% |
| graders | mixed | 2 | 135546 | 4.0 | 4.4m | 100% |
| graders | pass | 28 | 354528 | 12.1 | 4.5m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40463931792 | Rich issue triage | success | 6.9m | 10/0 | 395.2K | 14 | 0 | 0 |
| 40463833367 | Rich issue triage | success | 4.0m | 8/0 | 294.6K | 13 | 0 | 0 |
| 40463732575 | Rich issue triage | success | 4.3m | 7/0 | 237.9K | 9 | 0 | 0 |
| 40463629518 | Rich issue triage | success | 4.8m | 7/0 | 244.4K | 10 | 0 | 0 |
| 40463532019 | Rich issue triage | success | 4.4m | 9/0 | 342.1K | 12 | 0 | 0 |
| 40463431620 | Rich issue triage | success | 4.1m | 7/0 | 235.6K | 9 | 0 | 0 |
| 40463331749 | Rich issue triage | success | 4.4m | 5/0 | 135.4K | 4 | 0 | 0 |
| 40463230999 | Rich issue triage | success | 4.4m | 5/0 | 135.6K | 4 | 0 | 0 |
| 40463133306 | Rich issue triage | success | 5.1m | 8/0 | 300.8K | 11 | 0 | 0 |
| 40463034960 | Rich issue triage | success | 4.1m | 11/0 | 464.6K | 13 | 0 | 0 |
| 40462928924 | Rich issue triage | success | 4.5m | 7/0 | 237.9K | 9 | 0 | 0 |
| 40462830430 | Rich issue triage | success | 4.0m | 8/0 | 296.4K | 10 | 0 | 0 |
| 40462728385 | Rich issue triage | success | 4.3m | 8/0 | 288.4K | 10 | 0 | 0 |
| 40462627939 | Rich issue triage | success | 4.3m | 12/0 | 506.7K | 17 | 0 | 0 |
| 40462530161 | Rich issue triage | success | 4.3m | 9/0 | 345.8K | 12 | 0 | 0 |
| 40462425796 | Rich issue triage | success | 4.0m | 9/0 | 351.8K | 10 | 0 | 0 |
| 40462329057 | Rich issue triage | success | 4.2m | 12/0 | 507.7K | 16 | 0 | 0 |
| 40462231611 | Rich issue triage | success | 4.8m | 8/0 | 300.3K | 12 | 0 | 0 |
| 40462132644 | Rich issue triage | success | 3.9m | 9/0 | 344.7K | 13 | 0 | 0 |
| 40462033277 | Rich issue triage | success | 4.1m | 9/0 | 347.4K | 13 | 0 | 0 |
| 40461931449 | Rich issue triage | success | 5.5m | 9/0 | 358.1K | 12 | 0 | 0 |
| 40461831601 | Rich issue triage | success | 4.7m | 12/0 | 527.6K | 16 | 0 | 0 |
| 40461730311 | Rich issue triage | success | 4.6m | 9/0 | 344.0K | 12 | 0 | 0 |
| 40461629741 | Rich issue triage | success | 4.7m | 14/0 | 629.7K | 20 | 0 | 0 |
| 40461529127 | Rich issue triage | success | 4.2m | 7/0 | 236.5K | 6 | 0 | 0 |
| 40461419644 | Rich issue triage | success | 4.4m | 10/0 | 395.9K | 14 | 0 | 0 |
| 40461321916 | Rich issue triage | success | 5.6m | 12/0 | 509.6K | 15 | 0 | 0 |
| 40461225993 | Rich issue triage | success | 4.0m | 7/0 | 237.0K | 9 | 0 | 0 |
| 40461127987 | Rich issue triage | success | 4.6m | 7/0 | 239.3K | 9 | 0 | 0 |
| 40461027330 | Rich issue triage | success | 4.6m | 10/0 | 406.6K | 13 | 0 | 0 |

