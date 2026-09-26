---
name: "ai-bubble-burst-model"
version: "0.1.0"
status: "active"
created: "2026-09-26"
goal: "Build a first-principles economic and financial model simulating the impact of an AI bubble burst on the US labor market, the banking system / private credit, and the S&P 500."
deadline: "2026-10-15"
downstream: []
dod:
  - "Economic specification document (spec-ai-bubble-economic-model.md) defining labor displacement, capex payback deficit, banking contagion channels, and S&P 500 cohort valuation mechanics."
  - "Python simulation engine (repo/src/) implementing labor displacement, debt impairment stress-tests, and S&P 500 valuation waterfalls."
  - "Comprehensive test suite with automated assertions (repo/tests/)."
  - "Interactive web dashboard / scenario simulator (repo/src/dashboard.html) for stress-testing multi-variable shock parameters in real time."
  - "Comprehensive research report (docs/ai-bubble-burst-report.md) analyzing macroeconomic fallout, systemic bank risks, and market drawdown trajectories."
active_plan: "artifacts/plans/v1.0.0-2026-09-26-ai-bubble-burst-model.md"
strategy: ~
roadmap: ~
csa:
  spec_threshold: 90
  doc_threshold: 50
  doc_gate: soft
has_rules: false
last_reviewed: "2026-09-26"
tags: ["finance", "macroeconomics", "ai-bubble", "banking-crisis", "sp500", "valuation"]
milestones: []
---

# Project: ai-bubble-burst-model

## Goal

Build a rigorous, first-principles economic and financial model simulating the impact of an AI bubble burst. Specifically evaluate the mismatch between multi-trillion-dollar infrastructure CapEx and realistic knowledge worker displacement (5-10% economy-wide, ~20% junior/mid in tech, law, finance, consulting, customer ops, administrative, creative), quantify the transmission mechanisms of AI infrastructure debt into commercial and shadow banking, and model the resulting peak-to-trough crash dynamics across the S&P 500.

## Scope

- **In-Scope**:
  - Labor displacement modeling across 7 high-exposure white-collar occupational categories using BLS benchmarks, segmented by seniority tiers (Junior/Mid vs. Senior/Principal).
  - Return on Invested Capital (ROIC) deficit modeling comparing annual Big-4/global AI CapEx + depreciation against addressable enterprise software revenue capture.
  - Financial system & banking exposure mapping:
    - GPU-backed debt and Delayed Draw Term Loans (DDTLs) for neo-clouds.
    - Commercial bank fund-level leverage and subscription lines to private credit lenders.
    - Data center commercial real estate (CMBS) and utility/power grid debt expansion.
    - Regulated commercial bank CET1 capital ratio stress testing under credit loss scenarios.
  - S&P 500 constituent waterfall valuation model (AI Enablers, Hyperscalers, Infrastructure/Utilities, and S&P 480 Non-Tech).
  - Standalone interactive HTML/JS scenario dashboard and Python calculation engine with automated tests.
- **Out-of-Scope**:
  - High-frequency algorithmic trading strategies or day-to-day tick forecasting.
  - Deep technical analysis of proprietary model architectures beyond their economic compute efficiency.

## Definition of Done

- Economic specification document (`artifacts/specs/spec-ai-bubble-economic-model.md`) approved.
- Python simulation engine (`repo/src/`) passing all automated unit and scenario tests (`repo/tests/`).
- Interactive dashboard (`repo/src/dashboard.html`) operational for multi-scenario sensitivity exploration.
- Detailed analytical research report (`docs/ai-bubble-burst-report.md`) generated.

## Links

- GitHub: [Modeling-The-AI-Bubble-Crash](https://github.com/tboats/Modeling-The-AI-Bubble-Crash)
- Backlog: `artifacts/tasks/backlog.md`
- Active Plan: `artifacts/plans/v1.0.0-2026-09-26-ai-bubble-burst-model.md`
- Sessions: `sessions/`
