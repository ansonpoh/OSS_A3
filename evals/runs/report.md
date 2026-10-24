# Audit Report — Cross-Run Analysis

## Executive Summary

| Metric | Value |
|--------|-------|
| Runs analyzed | 1 |
| Runs with firewall data | 1 |
| Runs without firewall data | 0 |
| Total requests | 35 |
| Allowed requests | 35 |
| Blocked requests | 0 |
| Overall denial rate | 0.0% |
| Unique domains | 1 |

## Metrics Trends

| Metric | Total | Avg/run | Min | Max | Spikes |
|--------|-------|---------|-----|-----|--------|
| Token Trend | 372835 | 372835 | 372835 | 372835 | — |
| Turns | 1 | 1.0 | — | 1 | — |
| Duration | — | 5.8m | 5.8m | 5.8m | — |

## MCP Server Health (1 runs)

| Server | Connected | Error Rate | Total Calls | Errors | Status |
|--------|-----------|------------|-------------|--------|--------|
| `safeoutputs` | 1/1 | 0.0% | 2 | 0 | ✅ ok |

## Domain Inventory

| Domain | Status | Seen In | Allowed | Blocked |
|--------|--------|---------|---------|--------|
| `api.openai.com:443` | ✅ allowed | 1/1 runs | 35 | 0 |

## Agent Event Pattern Analysis

| Severity | Category | Title | Summary |
|----------|----------|-------|--------|
| ℹ info | execution | Cross-run log template patterns | Mined 2 distinct event templates across 6 pipeline stages from 2 events in 1 runs. (plan=1 finish=1) |

## Per-Run Breakdown

| Run ID | Workflow | Conclusion | Duration | Firewall | Tokens | Turns | MCP Err | Errors |
|--------|----------|------------|----------|----------|--------|-------|---------|--------|
| 40110297164 | Rich issue triage | success | 5.8m | 35/0 | 372.8K | 1 | 0 | 0 |

