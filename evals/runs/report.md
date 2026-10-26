# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 30 |
| Runs with firewall data | 30 |
| Runs without firewall data | 0 |
| Total requests | 260 |
| Allowed requests | 260 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 9853269 | 328442 | 135232 | 577975 | — |
| Turns | 344 | 11.5 | — | 16 | — |
| Duration | — | 4.6m | 4.0m | 5.8m | — |

## MCP Server Health (30 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 30/30 | 0.0% | 46 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 30/30 runs | 260 | 0 |

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
| execution_style | adaptive | 8 | 238356 | 9.0 | 4.7m | 100% |
| execution_style | directed | 2 | 135252 | 4.0 | 4.1m | 100% |
| execution_style | exploratory | 20 | 383795 | 13.2 | 4.7m | 100% |
| resource_profile | heavy | 18 | 393480 | 13.6 | 4.7m | 100% |
| resource_profile | lean | 2 | 135252 | 4.0 | 4.1m | 100% |
| resource_profile | moderate | 10 | 250011 | 9.2 | 4.7m | 100% |
| graders | mixed | 2 | 135252 | 4.0 | 4.1m | 100% |
| graders | pass | 28 | 342241 | 12.0 | 4.7m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40307040061 | Rich issue triage | success | 4.8m | 11/0 | 446.0K | 16 | 0 | 0 |
| 40306908868 | Rich issue triage | success | 4.7m | 8/0 | 294.9K | 13 | 0 | 0 |
| 40306773804 | Rich issue triage | success | 4.8m | 7/0 | 236.9K | 9 | 0 | 0 |
| 40306639285 | Rich issue triage | success | 5.3m | 8/0 | 295.3K | 10 | 0 | 0 |
| 40306499971 | Rich issue triage | success | 4.6m | 9/0 | 342.7K | 12 | 0 | 0 |
| 40306366315 | Rich issue triage | success | 4.8m | 7/0 | 235.3K | 9 | 0 | 0 |
| 40306236807 | Rich issue triage | success | 4.2m | 5/0 | 135.2K | 4 | 0 | 0 |
| 40306103576 | Rich issue triage | success | 4.0m | 5/0 | 135.3K | 4 | 0 | 0 |
| 40305967981 | Rich issue triage | success | 4.0m | 10/0 | 386.3K | 9 | 0 | 0 |
| 40305828678 | Rich issue triage | success | 4.8m | 9/0 | 351.2K | 12 | 0 | 0 |
| 40305696093 | Rich issue triage | success | 5.2m | 7/0 | 237.9K | 9 | 0 | 0 |
| 40305562319 | Rich issue triage | success | 4.6m | 8/0 | 298.0K | 10 | 0 | 0 |
| 40305430021 | Rich issue triage | success | 4.3m | 7/0 | 238.7K | 9 | 0 | 0 |
| 40305294545 | Rich issue triage | success | 4.5m | 10/0 | 401.5K | 14 | 0 | 0 |
| 40305155788 | Rich issue triage | success | 5.1m | 8/0 | 292.8K | 12 | 0 | 0 |
| 40305022308 | Rich issue triage | success | 5.8m | 8/0 | 245.1K | 9 | 0 | 0 |
| 40304891357 | Rich issue triage | success | 4.7m | 9/0 | 346.0K | 14 | 0 | 0 |
| 40304758239 | Rich issue triage | success | 4.7m | 10/0 | 405.3K | 15 | 0 | 0 |
| 40304623217 | Rich issue triage | success | 4.7m | 8/0 | 296.3K | 13 | 0 | 0 |
| 40304487135 | Rich issue triage | success | 5.1m | 12/0 | 507.9K | 15 | 0 | 0 |
| 40304354327 | Rich issue triage | success | 4.5m | 9/0 | 357.1K | 12 | 0 | 0 |
| 40304224721 | Rich issue triage | success | 4.8m | 13/0 | 578.0K | 15 | 0 | 0 |
| 40304089582 | Rich issue triage | success | 4.8m | 12/0 | 503.1K | 15 | 0 | 0 |
| 40303947621 | Rich issue triage | success | 4.7m | 11/0 | 455.5K | 16 | 0 | 0 |
| 40303812296 | Rich issue triage | success | 4.2m | 7/0 | 237.2K | 9 | 0 | 0 |
| 40303683457 | Rich issue triage | success | 4.2m | 10/0 | 403.0K | 14 | 0 | 0 |
| 40303551580 | Rich issue triage | success | 4.7m | 8/0 | 299.7K | 13 | 0 | 0 |
| 40303420148 | Rich issue triage | success | 4.1m | 7/0 | 236.3K | 9 | 0 | 0 |
| 40303286331 | Rich issue triage | success | 4.3m | 7/0 | 239.4K | 9 | 0 | 0 |
| 40303148670 | Rich issue triage | success | 4.6m | 10/0 | 415.5K | 14 | 0 | 0 |

