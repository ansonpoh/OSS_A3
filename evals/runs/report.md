# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 29 |
| Runs with firewall data | 29 |
| Runs without firewall data | 0 |
| Total requests | 243 |
| Allowed requests | 243 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 9101414 | 313841 | 134930 | 517719 | — |
| Turns | 330 | 11.4 | — | 15 | — |
| Duration | — | 4.6m | 3.9m | 5.6m | — |

## MCP Server Health (29 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 29/29 | 0.0% | 45 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 29/29 runs | 243 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 58 events in 29 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant graders: pass | 93% of runs share graders="pass" (27/29). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 6 | 236965 | 9.0 | 4.3m | 100% |
| execution_style | directed | 2 | 135026 | 4.0 | 4.6m | 100% |
| execution_style | exploratory | 21 | 352836 | 12.8 | 4.7m | 100% |
| resource_profile | heavy | 16 | 365389 | 13.4 | 4.8m | 100% |
| resource_profile | lean | 2 | 135026 | 4.0 | 4.6m | 100% |
| resource_profile | moderate | 11 | 271375 | 9.7 | 4.3m | 100% |
| graders | mixed | 2 | 135026 | 4.0 | 4.6m | 100% |
| graders | pass | 27 | 327087 | 11.9 | 4.6m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40298692208 | Rich issue triage | success | 4.3m | 11/0 | 452.4K | 15 | 0 | 0 |
| 40298564032 | Rich issue triage | success | 3.9m | 7/0 | 237.4K | 9 | 0 | 0 |
| 40298436201 | Rich issue triage | success | 4.5m | 9/0 | 347.3K | 11 | 0 | 0 |
| 40298309975 | Rich issue triage | success | 4.2m | 9/0 | 342.1K | 12 | 0 | 0 |
| 40298182854 | Rich issue triage | success | 4.3m | 7/0 | 234.5K | 9 | 0 | 0 |
| 40298051040 | Rich issue triage | success | 4.3m | 5/0 | 134.9K | 4 | 0 | 0 |
| 40297925341 | Rich issue triage | success | 5.0m | 5/0 | 135.1K | 4 | 0 | 0 |
| 40297799599 | Rich issue triage | success | 4.4m | 9/0 | 346.4K | 11 | 0 | 0 |
| 40297672285 | Rich issue triage | success | 4.6m | 9/0 | 347.7K | 12 | 0 | 0 |
| 40297544368 | Rich issue triage | success | 4.6m | 8/0 | 286.9K | 10 | 0 | 0 |
| 40297416800 | Rich issue triage | success | 4.2m | 9/0 | 336.1K | 11 | 0 | 0 |
| 40297290718 | Rich issue triage | success | 4.4m | 7/0 | 240.2K | 9 | 0 | 0 |
| 40297165175 | Rich issue triage | success | 4.2m | 9/0 | 344.3K | 15 | 0 | 0 |
| 40297040075 | Rich issue triage | success | 4.4m | 8/0 | 295.6K | 13 | 0 | 0 |
| 40296918840 | Rich issue triage | success | 4.3m | 7/0 | 246.6K | 10 | 0 | 0 |
| 40296789864 | Rich issue triage | success | 4.9m | 8/0 | 292.8K | 13 | 0 | 0 |
| 40296663804 | Rich issue triage | success | 5.6m | 10/0 | 397.3K | 13 | 0 | 0 |
| 40296541889 | Rich issue triage | success | 4.7m | 8/0 | 293.9K | 13 | 0 | 0 |
| 40296416691 | Rich issue triage | success | 5.4m | 8/0 | 296.2K | 13 | 0 | 0 |
| 40296285483 | Rich issue triage | success | 5.1m | 8/0 | 311.5K | 13 | 0 | 0 |
| 40296156040 | Rich issue triage | success | 5.1m | 12/0 | 517.7K | 14 | 0 | 0 |
| 40296033177 | Rich issue triage | success | 4.5m | 9/0 | 344.6K | 13 | 0 | 0 |
| 40295913059 | Rich issue triage | success | 5.0m | 11/0 | 456.3K | 15 | 0 | 0 |
| 40295788739 | Rich issue triage | success | 4.4m | 7/0 | 235.5K | 9 | 0 | 0 |
| 40295668490 | Rich issue triage | success | 5.0m | 11/0 | 452.9K | 15 | 0 | 0 |
| 40295542775 | Rich issue triage | success | 4.8m | 9/0 | 348.3K | 13 | 0 | 0 |
| 40295421532 | Rich issue triage | success | 4.7m | 7/0 | 235.5K | 9 | 0 | 0 |
| 40295302407 | Rich issue triage | success | 4.2m | 7/0 | 238.8K | 9 | 0 | 0 |
| 40295183542 | Rich issue triage | success | 4.5m | 9/0 | 352.6K | 13 | 0 | 0 |

