# Modeling the AI Bubble Crash: First-Principles Macro & Financial Transmission

> A quantitative, first-principles model evaluating the macroeconomic and stock market impact of an AI bubble burst.

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests: Pytest](https://img.shields.io/badge/Tests-13%20Passed-brightgreen.svg)]()

---

## ⚡ Executive Summary

What happens if the multi-trillion-dollar investment in AI infrastructure faces diminishing returns, and the best it can do is replace **5% to 10% of overall knowledge workers** (~20% junior/mid-level staff in technical and professional services, while failing to displace senior decision-makers due to legal and fiduciary accountability)?

This model mathematically connects:
1. **The White-Collar Labor Displacement Ceiling**: Benchmarking 18.0M US workers across 7 high-exposure occupational categories (BLS data).
2. **The CapEx Payback Deficit**: The negative Return on Invested Capital (ROIC) trap facing hyperscalers due to 3-to-4-year GPU depreciation schedules.
3. **The Financial & Banking System Debt Stack**: Tracing \$668B in debt through GPU-backed term loans, private credit subscription lines, bridge loans, and utility bonds.
4. **S&P 500 Waterfall Drawdown**: An algebraic 4-cohort decomposition modeling why the S&P 500 experiences a **-40.1% peak-to-trough crash** (falling from 5,750 down to 3,445).

---

## 📊 Core Findings

| Dimension | Modeled Baseline Output | Mechanism / Driver |
| :--- | :--- | :--- |
| **Gross Labor Wage Savings** | **\$221.5 Billion / year** | Displacing ~20% junior / 10% mid across 18M knowledge workers. |
| **Addressable Software Revenue** | **\$39.9 Billion / year** | Enterprise customers capture the majority of surplus; IT vendors capture ~18%. |
| **Big-4 Sustaining Carrying Cost** | **\$202.9 Billion / year** | Hardware D&A (4-year life) + data center power on \$710B CapEx. |
| **Net Big-4 Operating Deficit** | **-\$163.1 Billion / year** | **-23.0% ROIC** on infrastructure investments. |
| **Total At-Risk Debt Stack** | **\$668.0 Billion** | GPU DDTLs (\$68B), Bank-to-Private Credit lines (\$220B), CRE (\$145B), Utilities (\$180B). |
| **Commercial Bank Capital Hit** | **-\$43.4B CET1 (-56 bps)** | Generates an implied **\$434B macro credit contraction** (10x multiplier). |
| **S&P 500 Peak-to-Trough Drawdown** | **-40.1% (5,750 &rarr; 3,445)** | Semis (-86.5%), Hyperscalers (-46.9%), Utilities (-42.7%), S&P 480 (-25.3%). |

---

## 📉 S&P 500 Waterfall Drawdown: Mathematical Derivation

The index drawdown is derived algebraically from the weighted price returns of each cohort, driven by earnings per share ($\text{EPS}_c$) and forward valuation multiples $((P/E)_c)$:

$$\Delta P_{\text{index}} = \sum_{c=1}^{4} w_c \cdot \Delta P_c = \sum_{c=1}^{4} w_c \cdot \left[ (1 + \Delta \text{EPS}_c) \times \left( \frac{(P/E)_{c,\text{stressed}}}{(P/E)_{c,\text{base}}} \right) - 1 \right]$$

### Parameter Substitution (Base Crash Scenario: 45% CapEx Cut):

* **Cohort 1 (AI Enablers & Silicon: NVDA, AVGO, TSM, AMD)**:
  * $w_1 = 14.0\%, \quad \Delta \text{EPS}_1 = -75.9\%, \quad P/E: 38.5\text{x} \to 21.6\text{x}$
  * $\Delta P_1 = (1 - 0.759) \times (21.6 / 38.5) - 1 = \mathbf{-86.5\%}$ (Index Drag: **-12.11%**)
* **Cohort 2 (Hyperscalers & Big Tech: MSFT, GOOGL, AMZN, META)**:
  * $w_2 = 25.0\%, \quad \Delta \text{EPS}_2 = -25.2\%, \quad P/E: 31.0\text{x} \to 22.0\text{x}$
  * $\Delta P_2 = (1 - 0.252) \times (22.0 / 31.0) - 1 = \mathbf{-46.9\%}$ (Index Drag: **-11.73%**)
* **Cohort 3 (Power, Utilities & Data Center REITs: VST, CEG, DLR, EQIX)**:
  * $w_3 = 4.5\%, \quad \Delta \text{EPS}_3 = -15.8\%, \quad P/E: 27.0\text{x} \to 18.4\text{x}$
  * $\Delta P_3 = (1 - 0.158) \times (18.4 / 27.0) - 1 = \mathbf{-42.7\%}$ (Index Drag: **-1.92%**)
* **Cohort 4 (Broader S&P 480 Non-Tech: Financials, Healthcare, Consumer)**:
  * $w_4 = 56.5\%, \quad \Delta \text{EPS}_4 = -13.0\%, \quad P/E: 18.5\text{x} \to 15.9\text{x}$
  * $\Delta P_4 = (1 - 0.130) \times (15.9 / 18.5) - 1 = \mathbf{-25.3\%}$ (Index Drag: **-14.29%**)

$$\Delta P_{\text{index}} = -12.11\% - 11.73\% - 1.92\% - 14.29\% = \mathbf{-40.05\% \approx -40.1\%}$$

---

## 🛡️ Why This Crash Will Not Be as Deep as 2008 (-40% vs -57%)

1. **No Consumer Balance Sheet Insolvency**: 2008 was a household solvency crisis (millions of underwater homeowners defaulting on residential mortgages). The AI crash is a corporate asset write-down and CapEx retrenchment.
2. **Bank Capitalization is Substantially Stronger**: In 2007, global investment banks were levered 30:1 to 40:1 with negligible common equity. Today, Tier-1 Common Equity (CET1) ratios are ~12.2% with strict liquidity coverage ratios.
3. **Big Tech's Core Free Cash Flow Moats**: Unlike 2000 dot-coms or 2008 mortgage originators, hyperscalers generate hundreds of billions in non-AI high-margin cash flow (search advertising, e-commerce, cloud enterprise software, app stores), establishing an indestructible operating cash flow floor.
4. **Private Credit Shock Absorption**: A major share of GPU asset-backed debt and specialized data center financing is held by locked-up, long-duration private debt funds (Blackstone, Magnetar, Coatue) rather than fractional-reserve commercial banks vulnerable to demand-deposit runs.

---

## 🚀 Quickstart & Interactive Dashboard

### 1. View the Interactive HTML Report
Open [`docs/ai_bubble_burst_report.html`](./docs/ai_bubble_burst_report.html) directly in any modern web browser:
```bash
open docs/ai_bubble_burst_report.html
```
Features dynamic sliders, 6 responsive Chart.js plots, and live scenario stress-testing.

### 2. Run the Test Suite
```bash
pytest repo/tests/ -v
```

### 3. Re-run or Customize Model Simulations
```bash
python repo/src/labor_capex_model.py
python repo/src/banking_contagion_model.py
python repo/src/sp500_valuation_model.py
```
