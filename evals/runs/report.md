# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 30 |
| Runs with firewall data | 30 |
| Runs without firewall data | 0 |
| Total requests | 259 |
| Allowed requests | 259 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 9842281 | 328076 | 135526 | 557697 | — |
| Turns | 342 | 11.4 | — | 16 | — |
| Duration | — | 4.6m | 4.0m | 6.0m | — |

## MCP Server Health (30 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 30/30 | 0.0% | 46 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.anthropic.com:443` | ✅ allowed | 30/30 runs | 259 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 60 events in 30 runs. (finish=1 plan=1) |

## Cluster Patterns

| Severity | Kind | Title | Description |
|----------|------|-------|-------------|
| 🟡 low | style_skew | Dominant graders: pass | 90% of runs share graders="pass" (27/30). Low diversity may indicate homogeneous workload or classification bias. |

## Run Clusters

| Dimension | Value | Runs | Avg Tokens | Avg Turns | Avg Duration | Success Rate |
|-----------|-------|------|------------|-----------|--------------|-------------|
| execution_style | adaptive | 8 | 232130 | 8.5 | 4.5m | 100% |
| execution_style | directed | 2 | 135680 | 4.0 | 4.7m | 100% |
| execution_style | exploratory | 20 | 385693 | 13.3 | 4.7m | 100% |
| resource_profile | heavy | 17 | 401436 | 13.9 | 4.7m | 100% |
| resource_profile | lean | 1 | 135526 | 4.0 | 4.4m | 100% |
| resource_profile | moderate | 12 | 240194 | 8.5 | 4.5m | 100% |
| graders | mixed | 3 | 260350 | 7.0 | 4.7m | 100% |
| graders | pass | 27 | 335601 | 11.9 | 4.6m | 100% |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40321476014 | Rich issue triage | success | 4.5m | 12/0 | 497.6K | 16 | 0 | 0 |
| 40321348242 | Rich issue triage | success | 4.9m | 10/0 | 400.1K | 16 | 0 | 0 |
| 40321218100 | Rich issue triage | success | 4.2m | 6/0 | 188.4K | 8 | 0 | 0 |
| 40321082463 | Rich issue triage | success | 4.6m | 8/0 | 296.1K | 10 | 0 | 0 |
| 40320952379 | Rich issue triage | success | 4.5m | 8/0 | 294.3K | 12 | 0 | 0 |
| 40320825478 | Rich issue triage | success | 4.1m | 7/0 | 235.6K | 9 | 0 | 0 |
| 40320695713 | Rich issue triage | success | 4.4m | 5/0 | 135.5K | 4 | 0 | 0 |
| 40320568397 | Rich issue triage | success | 5.0m | 5/0 | 135.8K | 4 | 0 | 0 |
| 40320436479 | Rich issue triage | success | 4.0m | 8/0 | 298.0K | 10 | 0 | 0 |
| 40320310272 | Rich issue triage | success | 4.3m | 10/0 | 404.4K | 12 | 0 | 0 |
| 40320184696 | Rich issue triage | success | 4.7m | 7/0 | 238.0K | 9 | 0 | 0 |
| 40320056779 | Rich issue triage | success | 4.3m | 8/0 | 295.3K | 10 | 0 | 0 |
| 40319931523 | Rich issue triage | success | 6.0m | 7/0 | 239.0K | 9 | 0 | 0 |
| 40319802471 | Rich issue triage | success | 4.6m | 9/0 | 343.4K | 15 | 0 | 0 |
| 40319675443 | Rich issue triage | success | 4.4m | 10/0 | 403.5K | 14 | 0 | 0 |
| 40319549427 | Rich issue triage | success | 4.1m | 7/0 | 244.8K | 9 | 0 | 0 |
| 40319426127 | Rich issue triage | success | 4.3m | 9/0 | 344.3K | 15 | 0 | 0 |
| 40319299095 | Rich issue triage | success | 5.7m | 10/0 | 409.0K | 16 | 0 | 0 |
| 40319164231 | Rich issue triage | success | 4.9m | 9/0 | 343.3K | 12 | 0 | 0 |
| 40319044823 | Rich issue triage | success | 4.6m | 10/0 | 403.2K | 13 | 0 | 0 |
| 40318926791 | Rich issue triage | success | 5.0m | 9/0 | 357.5K | 12 | 0 | 0 |
| 40318807682 | Rich issue triage | success | 4.9m | 10/0 | 396.2K | 13 | 0 | 0 |
| 40318683302 | Rich issue triage | success | 5.7m | 13/0 | 557.7K | 16 | 0 | 0 |
| 40318557243 | Rich issue triage | success | 4.9m | 11/0 | 455.4K | 15 | 0 | 0 |
| 40318437648 | Rich issue triage | success | 4.0m | 7/0 | 237.2K | 9 | 0 | 0 |
| 40318316213 | Rich issue triage | success | 4.6m | 12/0 | 509.7K | 13 | 0 | 0 |
| 40318194286 | Rich issue triage | success | 4.5m | 9/0 | 349.2K | 12 | 0 | 0 |
| 40318075354 | Rich issue triage | success | 4.7m | 7/0 | 235.5K | 6 | 0 | 0 |
| 40317950463 | Rich issue triage | success | 4.1m | 7/0 | 238.5K | 9 | 0 | 0 |
| 40317828868 | Rich issue triage | success | 4.2m | 9/0 | 355.7K | 14 | 0 | 0 |

