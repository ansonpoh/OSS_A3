# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 29 |
| Runs with firewall data | 29 |
| Runs without firewall data | 0 |
| Total requests | 254 |
| Allowed requests | 254 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 9681514 | 333845 | 135161 | 624913 | — |
| Turns | 326 | 11.2 | — | 17 | — |
| Duration | — | 4.3m | 3.6m | 5.3m | — |

## MCP Server Health (29 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 29/29 | 0.0% | 45 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 29/29 runs | 254 | 0 |

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
| execution_style | adaptive | 6 | 236202 | 9.0 | 4.2m | 100% |
| execution_style | directed | 2 | 135286 | 4.0 | 3.8m | 100% |
| execution_style | exploratory | 21 | 380653 | 12.6 | 4.3m | 100% |
| resource_profile | heavy | 17 | 395169 | 13.2 | 4.4m | 100% |
| resource_profile | lean | 2 | 135286 | 4.0 | 3.8m | 100% |
| resource_profile | moderate | 10 | 269305 | 9.4 | 4.2m | 100% |
| graders | mixed | 2 | 135286 | 4.0 | 3.8m | 100% |
| graders | pass | 27 | 348553 | 11.8 | 4.3m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40276456488 | Rich issue triage | success | 4.1m | 10/0 | 394.5K | 13 | 0 | 0 |
| 40276357371 | Rich issue triage | success | 4.0m | 7/0 | 236.8K | 9 | 0 | 0 |
| 40276266236 | Rich issue triage | success | 3.9m | 11/0 | 442.8K | 10 | 0 | 0 |
| 40276172354 | Rich issue triage | success | 5.3m | 9/0 | 344.7K | 12 | 0 | 0 |
| 40276079719 | Rich issue triage | success | 4.4m | 7/0 | 234.5K | 9 | 0 | 0 |
| 40275988016 | Rich issue triage | success | 4.1m | 5/0 | 135.4K | 4 | 0 | 0 |
| 40275889270 | Rich issue triage | success | 3.6m | 5/0 | 135.2K | 4 | 0 | 0 |
| 40275798677 | Rich issue triage | success | 4.3m | 9/0 | 351.4K | 12 | 0 | 0 |
| 40275709189 | Rich issue triage | success | 4.8m | 10/0 | 402.6K | 13 | 0 | 0 |
| 40275618137 | Rich issue triage | success | 4.8m | 8/0 | 237.5K | 9 | 0 | 0 |
| 40275522854 | Rich issue triage | success | 4.0m | 8/0 | 299.2K | 10 | 0 | 0 |
| 40275428325 | Rich issue triage | success | 4.3m | 7/0 | 236.6K | 9 | 0 | 0 |
| 40275338746 | Rich issue triage | success | 4.4m | 10/0 | 399.6K | 14 | 0 | 0 |
| 40275247475 | Rich issue triage | success | 5.1m | 8/0 | 294.5K | 12 | 0 | 0 |
| 40275156443 | Rich issue triage | success | 4.1m | 7/0 | 246.2K | 10 | 0 | 0 |
| 40275067830 | Rich issue triage | success | 4.3m | 12/0 | 505.4K | 16 | 0 | 0 |
| 40274975369 | Rich issue triage | success | 4.2m | 8/0 | 299.4K | 13 | 0 | 0 |
| 40274880989 | Rich issue triage | success | 4.5m | 9/0 | 349.2K | 14 | 0 | 0 |
| 40274790387 | Rich issue triage | success | 4.2m | 12/0 | 506.2K | 17 | 0 | 0 |
| 40274703103 | Rich issue triage | success | 4.3m | 9/0 | 355.7K | 12 | 0 | 0 |
| 40274608626 | Rich issue triage | success | 4.4m | 13/0 | 624.9K | 14 | 0 | 0 |
| 40274509847 | Rich issue triage | success | 4.1m | 9/0 | 342.1K | 12 | 0 | 0 |
| 40274420665 | Rich issue triage | success | 4.3m | 11/0 | 451.5K | 14 | 0 | 0 |
| 40274328960 | Rich issue triage | success | 4.1m | 7/0 | 236.4K | 9 | 0 | 0 |
| 40274238324 | Rich issue triage | success | 4.3m | 10/0 | 395.5K | 11 | 0 | 0 |
| 40274147809 | Rich issue triage | success | 4.3m | 9/0 | 346.4K | 12 | 0 | 0 |
| 40274057084 | Rich issue triage | success | 3.9m | 7/0 | 235.4K | 9 | 0 | 0 |
| 40273966527 | Rich issue triage | success | 4.3m | 8/0 | 287.6K | 10 | 0 | 0 |
| 40273876965 | Rich issue triage | success | 4.3m | 9/0 | 354.3K | 13 | 0 | 0 |

