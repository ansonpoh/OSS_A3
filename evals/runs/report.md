# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 29 |
| Runs with firewall data | 29 |
| Runs without firewall data | 0 |
| Total requests | 316 |
| Allowed requests | 316 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 12631434 | 435566 | 134131 | 965162 | ⚠ #40261762094 |
| Turns | 404 | 13.9 | — | 24 | — |
| Duration | — | 4.3m | 3.7m | 5.0m | — |

## MCP Server Health (29 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 29/29 | 0.0% | 45 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 29/29 runs | 316 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 58 events in 29 runs. (plan=1 finish=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant graders: pass | 90% of runs share graders="pass" (26/29). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 5 | 233981 | 9.0 | 4.3m | 100% |
| execution_style | directed | 2 | 134147 | 4.0 | 4.1m | 100% |
| execution_style | exploratory | 22 | 508783 | 16.0 | 4.4m | 100% |
| resource_profile | heavy | 19 | 541262 | 16.8 | 4.4m | 100% |
| resource_profile | lean | 2 | 134147 | 4.0 | 4.1m | 100% |
| resource_profile | moderate | 8 | 259895 | 9.5 | 4.3m | 100% |
| graders | mixed | 3 | 411152 | 10.7 | 4.3m | 100% |
| graders | pass | 26 | 438383 | 14.3 | 4.4m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40263391415 | Rich issue triage | success | 4.1m | 10/0 | 386.4K | 13 | 0 | 0 |
| 40263307470 | Rich issue triage | success | 3.7m | 7/0 | 233.1K | 9 | 0 | 0 |
| 40263222650 | Rich issue triage | success | 4.3m | 9/0 | 338.9K | 11 | 0 | 0 |
| 40263130980 | Rich issue triage | success | 4.1m | 12/0 | 489.3K | 15 | 0 | 0 |
| 40263048886 | Rich issue triage | success | 4.2m | 10/0 | 381.2K | 12 | 0 | 0 |
| 40262966107 | Rich issue triage | success | 4.5m | 5/0 | 134.2K | 4 | 0 | 0 |
| 40262881927 | Rich issue triage | success | 3.7m | 5/0 | 134.1K | 4 | 0 | 0 |
| 40262798013 | Rich issue triage | success | 5.0m | 15/0 | 656.0K | 20 | 0 | 0 |
| 40262706241 | Rich issue triage | success | 4.1m | 15/0 | 589.2K | 18 | 0 | 0 |
| 40262619809 | Rich issue triage | success | 4.9m | 7/0 | 232.4K | 9 | 0 | 0 |
| 40262531449 | Rich issue triage | success | 4.6m | 7/0 | 236.9K | 9 | 0 | 0 |
| 40262442489 | Rich issue triage | success | 4.2m | 7/0 | 234.3K | 9 | 0 | 0 |
| 40262357547 | Rich issue triage | success | 4.2m | 14/0 | 600.4K | 21 | 0 | 0 |
| 40262270315 | Rich issue triage | success | 4.3m | 8/0 | 288.4K | 13 | 0 | 0 |
| 40262188151 | Rich issue triage | success | 4.3m | 8/0 | 289.8K | 10 | 0 | 0 |
| 40262103567 | Rich issue triage | success | 4.7m | 19/0 | 868.1K | 22 | 0 | 0 |
| 40262018915 | Rich issue triage | success | 4.4m | 9/0 | 340.7K | 13 | 0 | 0 |
| 40261935129 | Rich issue triage | success | 4.3m | 17/0 | 773.8K | 22 | 0 | 0 |
| 40261842065 | Rich issue triage | success | 4.4m | 15/0 | 600.7K | 21 | 0 | 0 |
| 40261762094 | Rich issue triage | success | 4.6m | 21/0 | 965.2K ⚠ | 24 | 0 | 0 |
| 40261683725 | Rich issue triage | success | 4.7m | 13/0 | 624.3K | 15 | 0 | 0 |
| 40261602559 | Rich issue triage | success | 4.6m | 20/0 | 856.8K | 22 | 0 | 0 |
| 40261520036 | Rich issue triage | success | 4.5m | 12/0 | 502.9K | 17 | 0 | 0 |
| 40261432923 | Rich issue triage | success | 4.2m | 7/0 | 233.3K | 9 | 0 | 0 |
| 40261351494 | Rich issue triage | success | 4.5m | 10/0 | 391.9K | 15 | 0 | 0 |
| 40261271112 | Rich issue triage | success | 4.0m | 9/0 | 335.9K | 12 | 0 | 0 |
| 40261186947 | Rich issue triage | success | 4.3m | 8/0 | 280.5K | 10 | 0 | 0 |
| 40261105456 | Rich issue triage | success | 4.5m | 9/0 | 337.3K | 12 | 0 | 0 |
| 40261020022 | Rich issue triage | success | 4.6m | 8/0 | 295.6K | 13 | 0 | 0 |

