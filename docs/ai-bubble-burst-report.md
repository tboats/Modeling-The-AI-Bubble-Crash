# The Anatomy of an AI Bubble Burst: Macroeconomic & Financial System Simulation Report

> **Project:** `ai-bubble-burst-model`  
> **Date:** September 2026  
> **Author:** Antigravity (Pair Programming with User)  
> **Status:** Final Analytical Report  
> **Interactive Dashboard Artifact:** [`docs/ai_bubble_burst_report.html`](file:///Users/tboats/Documents/Code/investing/META/Projects/ai-bubble-burst-model/docs/ai_bubble_burst_report.html)  

---

## ⚡ Executive Summary (TL;DR)

This report formalizes a first-principles quantitative model evaluating what occurs if generative AI capabilities reach an economic ceiling, achieving **5% to 10% overall workforce displacement** across the knowledge economy, concentrated at **~20% in junior and mid-level tiers of high-exposure white-collar professions** (software engineering, law, finance, customer ops, consulting, creative, administrative), while failing to displace senior decision-makers due to legal accountability and fiduciary liability.

### Key Takeaways:
1. **The Labor & Software Monetization Mismatch**: Displacing ~20% of junior and 10% of mid-level knowledge workers yields **~\$221.5 Billion** in gross annual wage savings. At historical enterprise software capture rates (18%), AI software vendors capture only **~\$39.9 Billion per year**.
2. **The Hyperscaler Payback Deficit**: The Big 4 hyperscalers (Microsoft, Alphabet, Amazon, Meta) are spending **~\$710 Billion/year** in 2026. Rapid 4-year accelerator depreciation creates a **-\$163.1 Billion annual carrying deficit (-23.0% ROIC)**, forcing a violent CapEx cut.
3. **The Banking System Debt Pipeline (\$668B)**: Debt entered through GPU-backed term loans, bank subscription credit lines to private credit funds, bridge loan warehouses, data center CMBS, and utility generation bonds. Commercial banks absorb **\$43.4 Billion in credit losses**, depleting CET1 capital ratios by **56 bps** and triggering **~\$434 Billion in general lending contraction**.
4. **S&P 500 Peak-to-Trough Drawdown (-40.1%)**: The index falls from **5,750 down to 3,445**. Silicon enablers plunge **-86.5%** (bullwhip effect), hyperscalers drop **-46.9%**, and the broader S&P 480 contracts **-25.3%**.

---

## 📉 Why the Crash Will Not Be as Deep as the 2008 Financial Crisis (-40% vs -57%)

While 3-year AI infrastructure spending (2024–2026: **~\$1.85 Trillion**) exceeds total peak subprime mortgage issuance (2004–2007: **\$1.35 Trillion**), four structural firewalls prevent an existential financial collapse on the order of 2008:

1. **No Systemic Consumer Balance Sheet Insolvency**: 2008 was fundamentally a household solvency crisis. Tens of millions of homeowners were underwater with negative equity, defaulting on mortgages, triggering foreclosures, and collapsing consumer spending across the entire economy. The AI bubble burst is a corporate asset impairment and CapEx correction, not a household balance-sheet insolvency.
2. **Bank Capitalization is Substantially Stronger (Post-Dodd-Frank)**: In 2007, global investment banks (Lehman Brothers, Bear Stearns, Merrill Lynch) were levered 30:1 to 40:1 with negligible tangible common equity. Today, Tier-1 Common Equity (CET1) ratios are ~12.2% with strict liquidity coverage ratios (LCR). The estimated commercial bank credit loss of \$43B to \$74B represents capital depletion, not systemic insolvency.
3. **Big Tech's Core Free Cash Flow Moats**: Unlike 2000 dot-com companies or 2008 mortgage originators, hyperscalers (Microsoft, Alphabet, Apple, Amazon) generate hundreds of billions in non-AI high-margin cash flow (search advertising, e-commerce, cloud enterprise software, mobile app stores), establishing an indestructible operating cash flow floor.
4. **Private Credit & Shadow Debt Shock Absorption**: A major share of GPU asset-backed debt and specialized data center financing is held by locked-up, long-duration private debt funds (Blackstone, Magnetar, Coatue) and sovereign wealth funds rather than fractional-reserve commercial banks vulnerable to demand-deposit bank runs.

## 💥 What Drives the Drop? The 4-Stage Mechanical Transmission Engine

The market does not drop from an emotional or arbitrary change in sentiment; it drops because of a **mathematical collision between front-loaded hardware depreciation and back-loaded software monetization**. 

Here is the exact mechanical chain from our first-principles model:

```
[ STAGE 1: ROIC COLLISION ]
Hyperscalers invest $710B in 2026 -> $203B/yr sustaining carrying costs (D&A + Power)
Enterprise software monetization tops out at ~$40B/yr (junior/mid replacement limits)
Result: -23% ROIC on CapEx -> Hyperscaler Boards force a 45% CapEx cut ($710B -> $390B)
             │
             ▼
[ STAGE 2: SEMICONDUCTOR BULLWHIP & OPERATING LEVERAGE (-86.5% DROP) ]
Hyperscalers pause orders to digest accumulated inventory backlog -> Chip orders fall 60%-75%
Fab fixed costs remain high -> Operating leverage works in reverse: Semis EPS craters -75.9%
Forward P/E multiple compresses from 38.5x bubble high to 21.6x cyclical trough
             │
             ▼
[ STAGE 3: HYPERSCALER MARGIN SQUEEZE & DE-RATING (-46.9% DROP) ]
$1.85T in past deployed CapEx cannot be unspent -> Depreciation hits income statement (-585 bps margin)
Cloud revenue growth slows from 25%+ to 4% -> Multiple de-rates from 31x compounder to 22x mature tech
             │
             ▼
[ STAGE 4: MACRO CONTAGION TO BROADER S&P 480 (-25.3% DROP) ]
Negative Wealth Effect: $18T in equity wealth wiped out -> Consumer discretionary spending contracts
Bank Balance Sheet Contraction: Commercial banks absorb $43.4B in debt losses across GPU loans & CMBS
Regulatory Capital Defense: Banks pull back $434B in general commercial credit lines (10x multiplier)
             │
             ▼
[ AGGREGATE S&P 500 PEAK-TO-TROUGH DRAWDOWN: -40.1% ]
(Index falls from 5,750 down to 3,445)
```

---

## 1. The Microeconomics of White-Collar Labor Displacement

### 1.1. Why Junior Displacement Cannot Fund the Bubble
A central paradox of the AI investment thesis is the assumption that displacing junior and mid-level personnel produces enough enterprise surplus to service trillion-dollar capital investments.

We benchmarked 7 high-exposure white-collar occupational categories using US Bureau of Labor Statistics (BLS) data:

```
Total High-Exposure Knowledge Workers: 18.0 Million
├── Junior Tier (40% headcount / 25% payroll): 7.2M workers @ $87k fully loaded avg
├── Mid Tier    (35% headcount / 35% payroll): 6.3M workers @ $138k fully loaded avg
└── Senior Tier (25% headcount / 40% payroll): 4.5M workers @ $210k fully loaded avg
```

In fields like legal services, software engineering, and auditing:
* **Senior workers are legally and structurally protected**: Senior software architects, trial attorneys, audit partners, and CFOs carry regulatory accountability, architectural signing authority, fiduciary liability, and client trust. AI tools can assist them, but cannot replace them without exposing corporations to existential legal risk.
* **Junior workers have lower payroll weights**: Junior developers, document review paralegals, and tier-1 customer agents make up only 25% of total payroll despite representing 40% of headcount.

```
                    GROSS ANNUAL WAGE SAVINGS BY SCENARIO
┌──────────────────────────────────────────────────────────┬─────────────────┬──────────────────┐
│ Scenario                                                 │ Workers Displaced│ Gross Wage Savings│
├──────────────────────────────────────────────────────────┼─────────────────┼──────────────────┤
│ Tech & Law Only (20% Junior/Mid in Tech & Law only)      │ 1.05 Million    │ \$110.0 Billion  │
│ Conservative Stagnation (10% Junior, 4% Mid across all) │ 0.97 Million    │ \$91.4 Billion   │
│ Base User Case (22% Junior, 10% Mid, 1.5% Senior across) │ 2.28 Million    │ \$221.5 Billion  │
│ Aggressive Automation (35% Junior, 20% Mid, 5% Senior)   │ 4.01 Million    │ \$403.2 Billion  │
└──────────────────────────────────────────────────────────┴─────────────────┴──────────────────┘
```

### 1.2. The Enterprise Software Capture Factor
Enterprise customers do not remit 100% of realized labor savings to AI vendors. Historically, enterprise IT and SaaS capture between **12% and 22%** of created productivity surplus (the remainder is retained as operating margin, returned to shareholders, or passed to consumers through price competition).

At an **18% capture ratio**:
$$\text{Addressable Software Revenue} = 18\% \times \$221.5\text{B} = \$39.9\text{ Billion per year}$$

Even under the most aggressive automation scenario imaginable (\$403B in wage savings), addressable AI enterprise software revenue tops out at **\$72.6 Billion annually**.

---

## 2. The CapEx Run-Rate & The Payback Deficit

### 2.1. The CapEx Explosion
Between 2024 and 2026, the Big 4 hyperscalers expanded annual CapEx from \$222B to **\$710B**:

* **Amazon**: ~\$205 Billion
* **Alphabet**: ~\$188 Billion
* **Microsoft**: ~\$182 Billion
* **Meta**: ~\$135 Billion
* **Global Total (including Apple, Oracle, Sovereign AI, CoreWeave)**: **\$1,050 Billion**

### 2.2. The Rapid Depreciation Trap
Unlike traditional infrastructure assets (such as railways, fiber-optic lines, or power plants) that amortize over 20 to 40 years, AI accelerators (GPUs, TPUs, custom ASICs, optical transceivers) face rapid efficiency degradation and obsolescence. Their economic useful life is **3 to 4 years**.

```
Annual Sustaining Burden (Big 4 in 2026):
  Hardware Depreciation (65% of CapEx over 4 years)  = $115.4 Billion
  Facility Shell Amortization (35% over 15 years)    = $16.6 Billion
  Data Center Power & Facility Cooling (10% of CapEx)= $71.0 Billion
  ───────────────────────────────────────────────────────────────
  Total Annual Carrying Cost                        = $202.9 Billion / year

Versus Addressable Software Revenue:
  Software Revenue (Base User Scenario)              = $39.9 Billion / year
  ───────────────────────────────────────────────────────────────
  NET ANNUAL DEFICIT (Big 4 Hyperscalers)           = -$163.1 Billion / year
  ROIC on 2026 CapEx                                = -23.0%
```

**Conclusion**: When hyperscaler management teams and institutional shareholders realize that new cluster deployments yield a -23% ROIC, CapEx is violently curtailed by **30% to 55%**.

---

## 3. The Financial System & Banking Nexus: Where the Debt Lives

The widely cited belief that *"AI spending cannot cause a financial crisis because tech companies have massive cash balances"* is an illusion. While tech giants began this cycle with pristine balance sheets, spending accelerated past operating cash flows in 2025–2026, creating a **\$668 Billion debt stack**:

```
                       [ $668B AT-RISK AI DEBT STACK ]
                                      │
   ┌───────────────┬──────────────────┼─────────────────┬────────────────┐
   ▼               ▼                  ▼                 ▼                ▼
Channel 1       Channel 2          Channel 3         Channel 4        Channel 5
Neo-Cloud DDTLs Bank Sub Lines     Warehouse Bridge  Data Center CMBS Utility Grid Debt
   $68B            $220B              $55B              $145B            $180B
(CoreWeave/GPU) (Blackstone/Apollo)(Wall St Desks)   (QTS/Digital R.) (Constellation)
   │               │                  │                 │                │
   └───────────────┴──────────────────┼─────────────────┴────────────────┘
                                      ▼
                  [ COMMERCIAL BANK CET1 CAPITAL EROSION ]
                  Base Loss: $43.4B  |  Severe Loss: $74.4B
                  Contraction Multiplier: 10x ($434B - $744B)
```

### The 5 Debt Transmission Channels:

1. **Neo-Cloud GPU DDTLs & ABS (\$68B)**:
   * CoreWeave alone expanded debt to over **\$35 Billion** via Delayed Draw Term Loans, secured against H100/Blackwell GPUs and take-or-pay startup contracts.
   * If compute demand collapses and hardware values plunge by 60%, loan recovery rates fall to 35 cents on the dollar, generating **~\$19.5B in direct credit losses**.
2. **Bank Subscription Credit Lines to Private Debt Funds (\$220B)**:
   * Major Wall Street banks (JPMorgan, Goldman Sachs, Morgan Stanley, Citigroup, Wells Fargo, MUFG) extended senior credit lines and NAV facilities to private credit funds (Blackstone, Magnetar, Coatue).
   * As private funds face illiquidity and default from tech borrowers, defaults on bank subscription facilities generate **~\$14.8B in commercial bank write-downs**.
3. **Wall Street Arranger Bridge Loans (\$55B)**:
   * Banks hold unplaced bridge facilities and warehouse loans on their trading books. In a sudden risk-off freeze, these become "hung debt," requiring **~\$13.8B in direct mark-to-market markdowns**.
4. **Data Center Commercial Mortgages & CMBS (\$145B)**:
   * Construction loans and CMBS secured by specialized data center shells face tenant renegotiations, generating **~\$6.6B in bank credit losses**.
5. **Regulated Utility & Grid Corporate Debt (\$180B)**:
   * Utilities issued billions in bonds to construct dedicated nuclear, gas, and transmission infrastructure for AI loads. Credit spread widening of 200 bps inflicts **~\$8.2B in mark-to-market losses** on bank bond holdings.

### Commercial Bank Balance Sheet Impact:
Across the Top 5 US Bank Holding Companies:
* Combined Baseline CET1 Capital: **\$950.0 Billion** (12.18% ratio).
* Base Case Credit Losses: **\$43.4 Billion**.
* Stressed CET1 Ratio: **11.62%** (depletion of **56 basis points**).
* **The Credit Contraction Multiplier**: To rebuild capital buffers and avoid regulatory scrutiny, banks reduce overall commercial and industrial lending by **10x the lost capital**, withdrawing **~\$434 Billion in liquidity from the real economy**.

---

## 4. S&P 500 Crash Waterfall: Anatomy of a -40.1% Drawdown

Because the S&P 500 is historically concentrated (the top 10 names represent ~38% of the index), a tech CapEx bust propagates through a four-stage waterfall:

```
                            S&P 500 WATERFALL DRAWDOWN
┌─────────────────────────────────┬──────────┬──────────┬──────────┬────────────┬─────────────┐
│ Cohort                          │ Weight   │ Base P/E │ Stress P/E│ EPS Impact │ Price Return│
├─────────────────────────────────┼──────────┼──────────┼──────────┼────────────┼─────────────┤
│ 1. AI Enablers & Silicon        │ 14.0%    │ 38.5x    │ 21.6x    │ -75.9%     │ -86.5%      │
│ 2. Hyperscalers & Big Tech      │ 25.0%    │ 31.0x    │ 22.0x    │ -25.2%     │ -46.9%      │
│ 3. Power, Utilities & REITs     │ 4.5%     │ 27.0x    │ 18.4x    │ -15.8%     │ -42.7%      │
│ 4. Broader S&P 480 Non-Tech     │ 56.5%    │ 18.5x    │ 15.9x    │ -13.0%     │ -25.3%      │
├─────────────────────────────────┼──────────┼──────────┼──────────┼────────────┼─────────────┤
│ S&P 500 INDEX TOTAL             │ 100.0%   │ 23.5x    │ 18.8x    │ -25.0%     │ -40.1%      │
└─────────────────────────────────┴──────────┴──────────┴──────────┴────────────┴─────────────┘
```

### Mathematical Derivation: Algebraic Formulation & Variable Substitution

Rather than an arbitrary estimate, the index drawdown is derived algebraically from the weighted price returns of each cohort, where each cohort price is the product of its earnings per share ($\text{EPS}_c$) and its valuation multiple $((P/E)_c)$:

#### 1. General Cohort Price Return Equation
$$\Delta P_c = \frac{P_{c,\text{stressed}} - P_{c,\text{base}}}{P_{c,\text{base}}} = (1 + \Delta \text{EPS}_c) \times \left[ \frac{(P/E)_{c,\text{stressed}}}{(P/E)_{c,\text{base}}} \right] - 1$$

#### 2. Aggregate S&P 500 Index Drawdown Equation
$$\Delta P_{\text{index}} = \sum_{c=1}^{4} w_c \cdot \Delta P_c = \sum_{c=1}^{4} w_c \cdot \left[ (1 + \Delta \text{EPS}_c) \times \left( \frac{(P/E)_{c,\text{stressed}}}{(P/E)_{c,\text{base}}} \right) - 1 \right]$$

**Where:**
* $w_c$: Index weighting of cohort $c$ ($\sum_{c=1}^{4} w_c = 1.0$).
* $\Delta \text{EPS}_c$: Percentage contraction in cohort earnings per share under the CapEx cut and operating leverage.
* $(P/E)_{c,\text{base}}$: Pre-crisis forward valuation multiple at bubble peak.
* $(P/E)_{c,\text{stressed}}$: De-rated forward multiple at cyclical trough.
* $\Delta P_c$: Net percentage price change of cohort $c$.

#### 3. Step-by-Step Parameter Substitution (Base Scenario: 45% CapEx Cut)

* **Cohort 1 (AI Enablers & Silicon)**:  
  $w_1 = 0.140, \quad \Delta \text{EPS}_1 = -75.9\%, \quad (P/E)_{1,\text{base}} = 38.5\text{x}, \quad (P/E)_{1,\text{stressed}} = 21.6\text{x}$  
  $$\Delta P_1 = (1 - 0.759) \times \left( \frac{21.6}{38.5} \right) - 1 = 0.241 \times 0.5610 - 1 = \mathbf{-86.5\%}$$  
  $$\text{Contribution}_1 = w_1 \cdot \Delta P_1 = 0.140 \times (-0.865) = \mathbf{-12.11\%}$$

* **Cohort 2 (Hyperscalers & Big Tech)**:  
  $w_2 = 0.250, \quad \Delta \text{EPS}_2 = -25.2\%, \quad (P/E)_{2,\text{base}} = 31.0\text{x}, \quad (P/E)_{2,\text{stressed}} = 22.0\text{x}$  
  $$\Delta P_2 = (1 - 0.252) \times \left( \frac{22.0}{31.0} \right) - 1 = 0.748 \times 0.7097 - 1 = \mathbf{-46.9\%}$$  
  $$\text{Contribution}_2 = w_2 \cdot \Delta P_2 = 0.250 \times (-0.469) = \mathbf{-11.73\%}$$

* **Cohort 3 (Power, Utilities & Data Center REITs)**:  
  $w_3 = 0.045, \quad \Delta \text{EPS}_3 = -15.8\%, \quad (P/E)_{3,\text{base}} = 27.0\text{x}, \quad (P/E)_{3,\text{stressed}} = 18.4\text{x}$  
  $$\Delta P_3 = (1 - 0.158) \times \left( \frac{18.4}{27.0} \right) - 1 = 0.842 \times 0.6815 - 1 = \mathbf{-42.7\%}$$  
  $$\text{Contribution}_3 = w_3 \cdot \Delta P_3 = 0.045 \times (-0.427) = \mathbf{-1.92\%}$$

* **Cohort 4 (Broader S&P 480 Non-Tech)**:  
  $w_4 = 0.565, \quad \Delta \text{EPS}_4 = -13.0\%, \quad (P/E)_{4,\text{base}} = 18.5\text{x}, \quad (P/E)_{4,\text{stressed}} = 15.9\text{x}$  
  $$\Delta P_4 = (1 - 0.130) \times \left( \frac{15.9}{18.5} \right) - 1 = 0.870 \times 0.8595 - 1 = \mathbf{-25.3\%}$$  
  $$\text{Contribution}_4 = w_4 \cdot \Delta P_4 = 0.565 \times (-0.253) = \mathbf{-14.29\%}$$

#### 4. Aggregate Index Result
$$\Delta P_{\text{index}} = (-12.11\%) + (-11.73\%) + (-1.92\%) + (-14.29\%) = \mathbf{-40.05\% \approx -40.1\%}$$
$$P_{\text{stressed}} = P_{\text{base}} \times (1 + \Delta P_{\text{index}}) = 5,750 \times (1 - 0.4005) = \mathbf{3,447 \quad (\text{Model Level: } 3,445)}$$

---

### Deconstructing the Cohort Movements:

1. **Cohort 1 (AI Enablers & Silicon: NVDA, AVGO, TSM, AMD, ASML) — -86.5% Drawdown**:
   * *Mechanism*: The **Semiconductor Bullwhip Effect**. When hyperscalers cut CapEx by 45%, chip purchases halt abruptly due to inventory backlogs. With 45% fixed fab and R&D costs, chipmaker EPS craters by **-75.9%**. Forward P/E compresses from 38.5x to 21.6x. This mirrors the historic collapses of Cisco (-88%) and Intel (-82%) between 2000 and 2002.
2. **Cohort 2 (Hyperscalers: MSFT, GOOGL, AMZN, META, AAPL) — -46.9% Drawdown**:
   * *Mechanism*: Cloud revenue growth decelerates from 25%+ down to mid-single digits. Multi-billion-dollar impairment charges on depreciating hardware compress operating margins by 585 bps. P/E multiples de-rate from 31.0x to 22.0x.
3. **Cohort 3 (Power, Utilities & Data Center REITs: VST, CEG, DLR, EQIX) — -42.7% Drawdown**:
   * *Mechanism*: Power producers that traded at tech-like compounder multiples (27x) revert back to traditional regulated utility multiples (18x) as long-term PPA pipelines are renegotiated.
4. **Cohort 4 (Broader S&P 480 Non-Tech: Financials, Healthcare, Industrials) — -25.3% Drawdown**:
   * *Mechanism*: The destruction of ~\$18 Trillion in tech equity wealth reduces consumer discretionary spending via the negative wealth effect (~3.5 cents per dollar lost), while bank credit contraction forces corporate IT budget freezes.

---

## 5. Comparative Matrix: 2008 Subprime Crisis vs. 2026 AI Bubble

| Dimension | 2008 Subprime Crisis | 2026 AI Infrastructure Bubble |
| :--- | :--- | :--- |
| **Capital Commitment** | ~\$1.35T in subprime originations | ~\$1.85T in 3-yr CapEx (2024–2026) |
| **Collateral Asset** | Physical real estate (slow depreciation) | Specialized GPUs/TPUs (3–4 yr obsolescence) |
| **Leverage Mechanism** | Off-balance-sheet SIVs, 30:1 bank leverage | Private credit DDTLs, bank subscription lines, SPVs |
| **Solvency Trigger** | Subprime mortgage defaults > 15% | Enterprise software revenue < \$50B vs \$200B+ D&A |
| **Bank Impact** | Solvency crisis (Bear Stearns, Lehman, AIG) | Capital depletion (-56 to -95 bps), credit pullback |
| **S&P 500 Trough** | -56.8% (over 17 months) | -40.1% base case (-52.2% in liquidity bust) |

---

## 6. Frontier AI Lab Micro-Foundations: The Anthropic S-1 (`ANT`) & The \$688.6B Compute Guillotine

On **October 26, 2026**, **Anthropic, PBC** filed its Form S-1 registration statement with the SEC (Nasdaq: **`ANT`**), providing the first audited financial look at a frontier AI lab. Rather than refuting the macroeconomic CapEx-to-Software deficit modeled in Sections 1 and 2, Anthropic’s S-1 exposes the exact microeconomic mechanism by which hyperscalers have **shifted hardware depreciation risk off their own income statements and onto frontier labs via non-cancelable take-or-pay compute contracts**.

### 6.1. Audited Unit Economics: Stripping Out Both GAAP Distortions
Anthropic’s S-1 contains two massive accounting distortions pointing in opposite directions:
1. **The `-\$80.75B` H1 2026 GAAP Net Loss is a Non-Cash Accounting Mirage**: Anthropic’s June 30, 2026 balance sheet lists `\$108.6B` in convertible notes payable on just **`\$6.2B` of actual principal** (held primarily by Amazon from 2023–2024 investments). Because Anthropic elected the ASC 825-10 fair-value option, valuation escalation triggered a **`-\$72.4B` non-cash mark-to-market charge** in H1 2026. These notes convert into Class N stock at IPO, leaving Anthropic debt-free with **`\$131.7B` in liquid reserves** (`\$112.4B` cash + `\$19.3B` marketable securities) and **`+\$3.93B` in H1 operating cash flow** (`+\$974M` Q2 GAAP operating profit on `\$11.56B` Q2 revenue).
2. **The `85.4%` Gross Margin is an Accounting Classification Illusion**: In Note 8 (Functional Expenses), Anthropic reports `\$2,380M` in Cost of Revenue on `\$16,286M` H1 2026 revenue (`85.4%` gross margin), but parks **`\$9,741M` of pre-training and research compute inside R&D**. Because frontier model weights become economically obsolete within 9–15 months, pre-training is recurring maintenance COGS, not long-lived capital R&D. Using the primary income statement’s **Total Compute & Infrastructure expense (`\$8,945M` in H1 2026)** yields a **true compute-adjusted gross margin of `45.1%`**—before deducting `\$3,808M` (`23.4%` of revenue) in Sales & Marketing, which is heavily weighted toward cloud marketplace revenue-share commissions on the `48%` of revenue routed through AWS, Google Cloud, and Azure.

### 6.2. Reconciling `\$16.29B` H1 Revenue (`\$46.22B` Q2 Run-Rate) with the Macro Payback Deficit
Why has Anthropic reached a `\$46.22B` annualized revenue run-rate with **`~900%` Net Revenue Retention (NRR)** when our Base Case macro model estimates `\$39.9B` (`\$72.6B` Aggressive Case) in domestic white-collar software capture?
* **First-Mover Capture of Software Engineering (`Claude Code`)**: In Section 1, US software engineering alone accounts for **`\$57.8B` in annual gross wage savings** (the single largest high-wage occupational pool). By dominating agentic coding (`Claude Code`) and global API workflows across 11,900+ enterprise accounts, Anthropic has captured the highest-elasticity global developer budget first.
* **The Off-Balance-Sheet Risk Transfer (`\$587.0B` Baseline / `\$688.6B` Post-Subsequent Events)**: To obtain its `\$131.7B` cash pile and compute access from Amazon, Google, and Microsoft, Anthropic signed **`\$265.6B` in fixed purchase commitments** plus **`\$321.4B` in uncommenced compute/data-center leases** as of June 30, 2026 (`\$587.0B`), expanding to **`~\$688.6B`** including Q3/October 2026 subsequent events:
  * **Google Cloud & Custom TPU Capacity**: `\$114.5B` direct take-or-pay cloud (Apr 2026–Jul 2033) + `\$137.5B` midpoint (`\$125B–\$150B`) additional TPU leases (2028–2031) = **`\$252.0B`**.
  * **Broadcom / Apollo Equipment & Data-Center Leases**: **`\$161.2B`** (2026–2034).
  * **SpaceX (xAI Infrastructure Subsidiary)**: Up to **`\$120.5B`** through 2029.
  * **Amazon Web Services (AWS)**: **`\$110.0B`** minimum take-or-pay infrastructure commitment.
  * **Microsoft Azure**: **`\$44.9B`** binding minimum commitment (Nov 2026–May 2033) *"regardless of actual usage."*
* **The `42.4%` Depreciation Transfer**: By 2028, Anthropic’s scheduled minimum compute outflow reaches **`~\$86.0B/year`**—which equals **`42.4%` of the Big-4 hyperscalers' entire `\$202.9B` annual carrying burden** modeled in Section 2.2. In effect, hyperscalers converted `\$131.7B` of private equity/convertible funding into `\$688.6B` of guaranteed multi-year cloud lease backlog.

### 6.3. Multi-Year Cash Flow & Valuation Waterfall (2026–2030 Simulation)
Our standalone simulation engine ([`anthropic_s1_model.py`](file:///Users/tboats/Documents/Code/investing/META/Projects/ai-bubble-burst-model/repo/src/anthropic_s1_model.py)) stress-tests Anthropic’s `\$131.7B` starting cash reserve (`\$146.7B` pro-forma with `\$15.0B` net IPO proceeds) against the ramping take-or-pay schedule across three scenarios:

| Scenario (Probability) | 2028E Revenue | 2028E Compute Outflow | 2026–30 Deadweight Compute | 2029E Cash Reserve | 2028E Implied Market Cap | Return vs. \$1.5T IPO | Solvency & Operational Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Bull: Agentic Singularity (20%)** | \$165.0B | \$86.0B | \$10.3B | **\$300.2B** | **\$2,610.2B** | **+74.0%** | `SOLVENT_SELF_FUNDING` |
| **2. Base: Rational Enterprise Plateau (50%)** | \$85.0B | \$77.4B | \$115.6B | **\$122.2B** | **\$844.7B** | **-43.7%** | `SOLVENT_CASH_BUFFER_BURN` |
| **3. Bear: AI Bubble Burst / Deflation (30%)** | \$40.0B | \$64.5B | \$182.9B | **\$52.4B** | **\$232.4B** | **-84.5%** | `SOLVENT_CASH_BUFFER_BURN` |
| **Probability-Weighted Expected Outcome** | — | — | — | **\$136.9B** | **\$1,014.1B** | **-32.4%** | Operational survivor; IPO overpriced at \$1.5T |

---

## 7. Accessing the Interactive HTML Dashboard

A fully interactive, single-file HTML simulation dashboard has been compiled and is accessible locally:
* **Interactive Dashboard File:** [`docs/ai_bubble_burst_report.html`](file:///Users/tboats/Documents/Code/investing/META/Projects/ai-bubble-burst-model/docs/ai_bubble_burst_report.html)
* **Python Simulation Modules:** [`labor_capex_model.py`](file:///Users/tboats/Documents/Code/investing/META/Projects/ai-bubble-burst-model/repo/src/labor_capex_model.py), [`banking_contagion_model.py`](file:///Users/tboats/Documents/Code/investing/META/Projects/ai-bubble-burst-model/repo/src/banking_contagion_model.py), [`sp500_valuation_model.py`](file:///Users/tboats/Documents/Code/investing/META/Projects/ai-bubble-burst-model/repo/src/sp500_valuation_model.py), and [`anthropic_s1_model.py`](file:///Users/tboats/Documents/Code/investing/META/Projects/ai-bubble-burst-model/repo/src/anthropic_s1_model.py).
* **Features Included:**
  * Dynamic sliders for Junior Displacement %, Mid Displacement %, Enterprise Capture %, CapEx Contraction %, and Multiple Compression %.
  * Real-time calculation of Gross Wage Savings, Software Revenue, Net CapEx Deficit, and S&P 500 Index Price Level.
  * Eight responsive Chart.js visualizations (including the new **Anthropic 2026–2030 Liquidity vs. Take-or-Pay Compute Floor Trajectory** and **\$688.6B Counterparty Commitment Breakdown**).
  * Comprehensive occupational, debt transmission, and Anthropic S-1 scenario waterfall tables.
