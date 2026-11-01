"""
Standalone HTML Report Generator for the Anthropic Form S-1 (ANT) Evaluation.
Generates a clean, zero-backslash interactive HTML report with Chart.js visualizations
and a live Take-or-Pay & Valuation Stress-Test Simulator.
"""

from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from anthropic_s1_model import AnthropicS1Model
from labor_capex_model import LaborCapexModel


def generate_anthropic_s1_html():
    s1_model = AnthropicS1Model()
    labor_model = LaborCapexModel()

    recon = s1_model.reconcile_s1_unit_economics()
    comm = s1_model.get_commitments_summary()
    scenarios_out = s1_model.run_predefined_s1_scenarios()
    macro_rec = s1_model.reconcile_with_macro_bubble_model(labor_model)

    bull_proj = scenarios_out["scenarios"]["agentic_singularity_bull"]["annual_projections"]
    base_proj = scenarios_out["scenarios"]["rational_enterprise_base"]["annual_projections"]
    bear_proj = scenarios_out["scenarios"]["ai_bubble_burst_bear"]["annual_projections"]

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anthropic Form S-1 (ANT) Independent Feasibility &amp; Valuation Evaluation</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
    <style>
        :root {{
            --bg-primary: #0a0e17;
            --bg-secondary: #121826;
            --bg-card: #1a2234;
            --text-primary: #f0f4f8;
            --text-secondary: #94a3b8;
            --accent-red: #ef4444;
            --accent-orange: #f97316;
            --accent-blue: #38bdf8;
            --accent-green: #10b981;
            --accent-purple: #a855f7;
            --accent-yellow: #eab308;
            --border-color: #2e3a52;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }}
        body {{
            background-color: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            padding: 24px;
        }}
        .container {{
            max-width: 1350px;
            margin: 0 auto;
        }}
        header {{
            background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
            border: 1px solid #4f46e5;
            border-radius: 16px;
            padding: 32px;
            margin-bottom: 24px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
        }}
        .nav-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
            font-size: 0.85rem;
        }}
        .nav-bar a {{
            color: var(--accent-blue);
            text-decoration: none;
            font-weight: 600;
            padding: 6px 12px;
            border-radius: 8px;
            background: rgba(56, 189, 248, 0.1);
            border: 1px solid rgba(56, 189, 248, 0.3);
        }}
        .nav-bar a:hover {{
            background: rgba(56, 189, 248, 0.2);
        }}
        header h1 {{
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 10px;
            background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        header p.subtitle {{
            font-size: 1.05rem;
            color: var(--text-secondary);
            max-width: 1080px;
        }}
        .meta-badges {{
            display: flex;
            gap: 10px;
            margin-top: 18px;
            flex-wrap: wrap;
        }}
        .badge {{
            padding: 5px 12px;
            border-radius: 9999px;
            font-size: 0.8rem;
            font-weight: 600;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-color);
        }}
        .badge.critical {{ background: rgba(239, 68, 68, 0.15); color: #fca5a5; border-color: rgba(239, 68, 68, 0.4); }}
        .badge.warning {{ background: rgba(249, 115, 22, 0.15); color: #fdba74; border-color: rgba(249, 115, 22, 0.4); }}
        .badge.info {{ background: rgba(56, 189, 248, 0.15); color: #7dd3fc; border-color: rgba(56, 189, 248, 0.4); }}
        .badge.success {{ background: rgba(16, 185, 129, 0.15); color: #6ee7b7; border-color: rgba(16, 185, 129, 0.4); }}

        .tldr-box {{
            background: linear-gradient(135deg, rgba(30, 27, 75, 0.6) 0%, rgba(15, 23, 42, 0.9) 100%);
            border: 2px solid #818cf8;
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 28px;
            box-shadow: 0 4px 20px rgba(129, 140, 248, 0.15);
        }}
        .tldr-box h2 {{
            color: #a5b4fc;
            font-size: 1.35rem;
            margin-bottom: 12px;
        }}
        .tldr-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
            margin-top: 14px;
        }}
        .tldr-item {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 15px 16px;
        }}
        .tldr-item h3 {{
            font-size: 0.95rem;
            color: #38bdf8;
            margin-bottom: 6px;
        }}
        .tldr-item p {{
            font-size: 0.88rem;
            color: #cbd5e1;
            line-height: 1.48;
        }}

        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }}
        .kpi-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .kpi-card .label {{
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-secondary);
            margin-bottom: 6px;
        }}
        .kpi-card .value {{
            font-size: 1.65rem;
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .kpi-card .subtext {{
            font-size: 0.8rem;
            color: var(--text-secondary);
        }}
        .value.red {{ color: var(--accent-red); }}
        .value.orange {{ color: var(--accent-orange); }}
        .value.blue {{ color: var(--accent-blue); }}
        .value.purple {{ color: var(--accent-purple); }}
        .value.green {{ color: var(--accent-green); }}

        .section {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 26px;
            margin-bottom: 26px;
        }}
        .section h2 {{
            font-size: 1.45rem;
            margin-bottom: 6px;
            color: #f8fafc;
        }}
        .section p.desc {{
            color: var(--text-secondary);
            margin-bottom: 20px;
            font-size: 0.95rem;
            max-width: 1100px;
        }}

        .chart-row {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(480px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}
        @media (max-width: 768px) {{
            .chart-row {{ grid-template-columns: 1fr; }}
        }}
        .chart-container {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px 20px;
            position: relative;
            height: 330px;
            display: flex;
            flex-direction: column;
        }}
        .chart-container h3 {{
            font-size: 0.95rem;
            margin-bottom: 10px;
            color: #e2e8f0;
            flex-shrink: 0;
        }}
        .chart-wrapper {{
            position: relative;
            flex-grow: 1;
            width: 100%;
            height: calc(100% - 30px);
        }}

        .simulator-panel {{
            background: linear-gradient(145deg, #131b2e 0%, #171f33 100%);
            border: 2px solid #38bdf8;
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 26px;
            box-shadow: 0 0 20px -5px rgba(56, 189, 248, 0.2);
        }}
        .simulator-panel h2 {{
            color: #38bdf8;
            font-size: 1.35rem;
            margin-bottom: 4px;
        }}
        .controls-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin: 18px 0;
        }}
        .control-group {{
            background: rgba(0, 0, 0, 0.28);
            padding: 12px 14px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.06);
        }}
        .control-group label {{
            display: flex;
            justify-content: space-between;
            font-size: 0.84rem;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        .control-group input[type="range"] {{
            width: 100%;
            height: 5px;
            background: #2e3a52;
            border-radius: 4px;
            outline: none;
            -webkit-appearance: none;
        }}
        .control-group input[type="range"]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #38bdf8;
            cursor: pointer;
            box-shadow: 0 0 6px rgba(56, 189, 248, 0.8);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 0.88rem;
        }}
        th, td {{
            padding: 10px 14px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}
        th {{
            background: rgba(255, 255, 255, 0.04);
            color: #94a3b8;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.05em;
        }}
        tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
        }}
        .align-right {{ text-align: right; }}
        .align-center {{ text-align: center; }}

        .callout {{
            border-left: 4px solid var(--accent-blue);
            background: rgba(56, 189, 248, 0.08);
            padding: 16px 20px;
            border-radius: 0 8px 8px 0;
            margin: 16px 0;
        }}
        .callout.danger {{
            border-left-color: var(--accent-red);
            background: rgba(239, 68, 68, 0.08);
        }}
        .callout.warning {{
            border-left-color: var(--accent-orange);
            background: rgba(249, 115, 22, 0.08);
        }}
        .callout.success {{
            border-left-color: var(--accent-green);
            background: rgba(16, 185, 129, 0.08);
        }}
        .callout h4 {{
            margin-bottom: 6px;
            font-size: 0.98rem;
        }}
        .callout p {{
            font-size: 0.88rem;
            color: #cbd5e1;
        }}

        .flow-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 14px;
            margin: 18px 0;
        }}
        .flow-step {{
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 16px;
            position: relative;
        }}
        .flow-step .step-tag {{
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--accent-blue);
            margin-bottom: 6px;
        }}
        .flow-step h4 {{
            font-size: 0.96rem;
            margin-bottom: 6px;
            color: #f8fafc;
        }}
        .flow-step p {{
            font-size: 0.83rem;
            color: #cbd5e1;
            line-height: 1.45;
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="nav-bar">
            <span style="color: #94a3b8;">SEC Form S-1 Deep Dive &bull; Filed October 26, 2026 &bull; Proposed Nasdaq Ticker: <strong>ANT</strong></span>
            <a href="ai_bubble_burst_report.html">&larr; View Full Macro AI Bubble Burst Dashboard</a>
        </div>
        <h1>Anthropic, PBC (Form S-1): Independent Feasibility &amp; Valuation Audit</h1>
        <p class="subtitle">
            Deconstructing Anthropic's $16.29B H1 2026 Revenue, the 85.4% vs. 45.1% Gross Margin Illusion, the $688.6B Off-Balance-Sheet Take-or-Pay Compute Guillotine, and Post-IPO Financial Scenarios (2026–2030).
        </p>
        <div class="meta-badges">
            <span class="badge info">H1 2026 Revenue: $16.29B (Q2 Run-Rate: $46.22B/yr)</span>
            <span class="badge success">Pre-IPO Liquid Cash Fortress: $131.7B</span>
            <span class="badge warning">True Compute-Adjusted Gross Margin: 45.1% (vs. 85.4% Accounting)</span>
            <span class="badge critical">Take-or-Pay &amp; Lease Commitments: $587.0B – $688.6B</span>
            <span class="badge">Expected Fair Value: $1.01T (vs. $1.5T IPO Target)</span>
        </div>
    </header>

    <!-- EXECUTIVE SUMMARY (TL;DR) -->
    <div class="tldr-box">
        <h2>⚡ Executive Verdict: Operational Winner, Capital-Structure Trap at $1.5T</h2>
        <p style="font-size: 0.95rem; color: #cbd5e1;">
            Anthropic's October 26, 2026 Form S-1 proves that frontier AI labs can generate tens of billions in real enterprise revenue, anchored by <strong>Claude Code</strong> and <strong>~900% Net Revenue Retention (NRR)</strong>. However, to secure the compute and capital required for that growth, Anthropic locked itself into <strong>$587.0B to $688.6B of non-cancelable multi-year take-or-pay infrastructure obligations</strong>—turning variable software economics into massive fixed operating leverage right at the peak of the AI capital cycle.
        </p>
        <div class="tldr-grid">
            <div class="tldr-item">
                <h3>1. Two Opposite GAAP Mirages</h3>
                <p>The headline <strong>-$80.75B H1 2026 GAAP net loss</strong> is a non-cash artifact of marking $6.2B in Amazon convertible notes up to $108.6B fair value (-$72.4B charge). Conversely, the <strong>85.4% accounting gross margin</strong> is inflated because $9.74B of recurring R&amp;D pre-training compute is excluded from COGS. True compute-adjusted gross margin is <strong>45.1%</strong>.</p>
            </div>
            <div class="tldr-item">
                <h3>2. The $688.6B Take-or-Pay Guillotine</h3>
                <p>As of June 30, 2026, Anthropic signed <strong>$265.6B in fixed purchase commitments</strong> + <strong>$321.4B in uncommenced leases ($587.0B)</strong>, surging to <strong>$688.6B</strong> with Q3/Oct 2026 deals (Google, Broadcom, SpaceX, AWS, Microsoft). Revenue must reach <strong>$140B–$160B/yr by 2028–2029</strong> to absorb ~$86B–$108B/yr in mandatory compute outflows.</p>
            </div>
            <div class="tldr-item">
                <h3>3. Financial Solvency vs. Valuation</h3>
                <p>Backed by <strong>$131.7B in cash and marketable securities</strong> ($146.7B post-IPO) and zero debt after note conversion, Anthropic <strong>will not go bankrupt</strong> even in a severe AI crash. However, in our 50% Base Case ($85B 2028E revenue), underutilized leases bleed cash down to $122.2B and compress fair value to <strong>~$845B (-43.7% vs. $1.5T IPO)</strong>.</p>
            </div>
            <div class="tldr-item">
                <h3>4. What Market Leanings Signal</h3>
                <p>Immediate institutional pushback forced initial <strong>$1.5T–$2.0T whisper valuations down toward $1.5T</strong> (with buy-side models clustering near $900B–$1.1T). Coming after the summer 2026 SpaceX mega-IPO, a $1.5T listing acts as a liquidity vacuum, signaling late-cycle risk transfer from hyperscalers to public equity portfolios.</p>
            </div>
        </div>
    </div>

    <!-- TOP KPI CARDS -->
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="label">Q2 2026 Annualized Run-Rate</div>
            <div class="value blue">$46.22B</div>
            <div class="subtext">$11.56B Q2 rev (+14x YoY in H1 2026)</div>
        </div>
        <div class="kpi-card">
            <div class="label">Q2 2026 GAAP Operating Profit</div>
            <div class="value green">+$974M</div>
            <div class="subtext">8.4% Q2 operating margin (+$3.93B H1 OCF)</div>
        </div>
        <div class="kpi-card">
            <div class="label">True Compute-Adjusted Margin</div>
            <div class="value orange">45.1%</div>
            <div class="subtext">vs. 85.4% accounting GM ($8.95B H1 compute)</div>
        </div>
        <div class="kpi-card">
            <div class="label">Pre-IPO Liquid Reserves</div>
            <div class="value purple">$131.70B</div>
            <div class="subtext">$112.4B cash + $19.3B short-term securities</div>
        </div>
        <div class="kpi-card">
            <div class="label">Total Infrastructure Commitments</div>
            <div class="value red">$688.60B</div>
            <div class="subtext">$587.0B June 30 baseline + subsequent events</div>
        </div>
        <div class="kpi-card">
            <div class="label">Probability-Weighted Fair Value</div>
            <div class="value orange">$1,014.1B</div>
            <div class="subtext">-32.4% downside vs. $1.5T IPO target</div>
        </div>
    </div>

    <!-- INTERACTIVE TAKE-OR-PAY & VALUATION STRESS TESTER -->
    <div class="simulator-panel">
        <h2>🎛️ Interactive Anthropic S-1 Take-or-Pay &amp; Valuation Stress-Tester (2026–2030)</h2>
        <p style="color: #94a3b8; font-size: 0.9rem;">
            Adjust 2028E enterprise revenue scale, organic compute intensity, emergency lease restructuring relief, and valuation multiples to test how Anthropic's $131.7B cash reserve absorbs its mandatory take-or-pay compute schedule ($22B in 2026 ramping to $86B in 2028 and $115B in 2030).
        </p>

        <div class="controls-grid">
            <div class="control-group">
                <label>
                    <span>2028E Annual Revenue ($B)</span>
                    <span id="simRev2028Val" style="color: #38bdf8;">$85B</span>
                </label>
                <input type="range" id="simRev2028Slider" min="30" max="200" step="5" value="85">
            </div>

            <div class="control-group">
                <label>
                    <span>Organic Compute Intensity (% Rev)</span>
                    <span id="simCompPctVal" style="color: #38bdf8;">50%</span>
                </label>
                <input type="range" id="simCompPctSlider" min="35" max="65" step="1" value="50">
            </div>

            <div class="control-group">
                <label>
                    <span>2028–30 Lease Restructuring Relief</span>
                    <span id="simReliefVal" style="color: #10b981;">10%</span>
                </label>
                <input type="range" id="simReliefSlider" min="0" max="40" step="5" value="10">
            </div>

            <div class="control-group">
                <label>
                    <span>2028E EV / Revenue Multiple</span>
                    <span id="simMultVal" style="color: #a855f7;">8.5x</span>
                </label>
                <input type="range" id="simMultSlider" min="4.0" max="18.0" step="0.5" value="8.5">
            </div>

            <div class="control-group">
                <label>
                    <span>Net IPO Cash Proceeds ($B)</span>
                    <span id="simIpoVal" style="color: #38bdf8;">$15B</span>
                </label>
                <input type="range" id="simIpoSlider" min="5" max="35" step="1" value="15">
            </div>
        </div>

        <div class="kpi-grid" style="margin-bottom: 0;">
            <div class="kpi-card" style="background: rgba(0,0,0,0.32);">
                <div class="label">2028E Actual Compute Outflow</div>
                <div class="value orange" id="outComp2028">$77.4B</div>
                <div class="subtext" id="outDeadweight2028">Unutilized penalty: $34.9B in 2028</div>
            </div>
            <div class="kpi-card" style="background: rgba(0,0,0,0.32);">
                <div class="label">2028E Compute-Adjusted Margin</div>
                <div class="value blue" id="outAdjMargin2028">8.9%</div>
                <div class="subtext" id="outOpMargin2028">GAAP Operating Margin: -19.1%</div>
            </div>
            <div class="kpi-card" style="background: rgba(0,0,0,0.32);">
                <div class="label">2029E Ending Liquid Reserves</div>
                <div class="value purple" id="outCash2029">$122.2B</div>
                <div class="subtext" id="outSolvencyTag">SOLVENT (Cash Buffer Absorbs Lease Deficit)</div>
            </div>
            <div class="kpi-card" style="background: rgba(0,0,0,0.32);">
                <div class="label">2028E Implied Market Cap</div>
                <div class="value red" id="outMcap2028">$844.7B</div>
                <div class="subtext" id="outReturnVsIpo" style="font-weight: 700; color: var(--accent-red);">-43.7% vs. $1.5T IPO Valuation</div>
            </div>
        </div>
    </div>

    <!-- SECTION 1: DECONSTRUCTING THE S-1 FINANCIALS -->
    <div class="section">
        <h2>📊 1. Deconstructing the S-1: Audited Financials vs. Accounting Mirages</h2>
        <p class="desc">
            In 2025, Anthropic transitioned its primary Consolidated Statements of Operations to a <strong>"nature of expense"</strong> layout while preserving the traditional <strong>"functional expense"</strong> breakdown in Note 8. Comparing both tables side-by-side exposes how accounting classification shapes the IPO narrative.
        </p>

        <div class="chart-row">
            <div class="chart-container">
                <h3>Quarterly Revenue Velocity ($M) &amp; Q2 2026 Operating Profit Inflection</h3>
                <div class="chart-wrapper">
                    <canvas id="quarterlyTrajectoryChart"></canvas>
                </div>
            </div>
            <div class="chart-container">
                <h3>H1 2026 Margin Waterfall: Accounting GM (85.4%) vs. Economic Reality</h3>
                <div class="chart-wrapper">
                    <canvas id="marginIllusionChart"></canvas>
                </div>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Consolidated Statements of Operations Line Item</th>
                    <th class="align-right">FY 2023</th>
                    <th class="align-right">FY 2024</th>
                    <th class="align-right">FY 2025</th>
                    <th class="align-right">H1 2025 (6M)</th>
                    <th class="align-right">H1 2026 (6M)</th>
                    <th class="align-right">% of H1 2026 Rev</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background: rgba(56, 189, 248, 0.08); font-weight: bold;">
                    <td><strong>Total Revenue</strong></td>
                    <td class="align-right">$41M</td>
                    <td class="align-right">$386M</td>
                    <td class="align-right">$4,585M</td>
                    <td class="align-right">$1,163M</td>
                    <td class="align-right">$16,286M</td>
                    <td class="align-right">100.0%</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&mdash; Usage / API ("Pay-for-Intelligence" Token Consumption)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">~$288M</td>
                    <td class="align-right">~$3,796M</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">$13,060M</td>
                    <td class="align-right">80.2%</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&mdash; Subscriptions (Claude Pro, Max, Team, Enterprise)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">~$98M</td>
                    <td class="align-right">~$789M</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">$3,226M</td>
                    <td class="align-right">19.8%</td>
                </tr>
                <tr>
                    <td colspan="7" style="background: rgba(255,255,255,0.03); color: #94a3b8; font-weight: 600; font-size: 0.78rem; text-transform: uppercase;">Primary Income Statement View (By Nature of Expense)</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&bull; Compute and Infrastructure (Inference + Pre-Training Total)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right" style="color: var(--accent-orange); font-weight: 600;">$8,945M</td>
                    <td class="align-right">54.9%</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&bull; Sales, Marketing, and Partnerships</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">$3,168M</td>
                    <td class="align-right">19.5%</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&bull; Personnel (Salaries, Benefits &amp; Stock-Based Compensation)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">$3,152M</td>
                    <td class="align-right">19.4%</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&bull; Other Operating and Administrative</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">$1,714M</td>
                    <td class="align-right">10.5%</td>
                </tr>
                <tr>
                    <td colspan="7" style="background: rgba(255,255,255,0.03); color: #94a3b8; font-weight: 600; font-size: 0.78rem; text-transform: uppercase;">Footnote View (Note 8 — By Functional Classification)</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&bull; Cost of Revenue (Direct Customer-Serving Inference Only)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">$1,023M</td>
                    <td class="align-right">$2,380M</td>
                    <td class="align-right">14.6% (85.4% GM)</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&bull; Research and Development (Pre-Training Compute + Research Staff)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right" style="color: var(--accent-red); font-weight: 600;">$9,741M</td>
                    <td class="align-right">59.8%</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&bull; Sales and Marketing (Cloud Marketplace Fees + Free Tier Compute)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">$3,808M</td>
                    <td class="align-right">23.4%</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&bull; General and Administrative</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">$1,050M</td>
                    <td class="align-right">6.4%</td>
                </tr>
                <tr style="font-weight: bold;">
                    <td><strong>Total Operating Expenses</strong></td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">~$12,585M</td>
                    <td class="align-right">$3,298M</td>
                    <td class="align-right">$16,979M</td>
                    <td class="align-right">104.3%</td>
                </tr>
                <tr style="background: rgba(249, 115, 22, 0.08); font-weight: bold;">
                    <td><strong>GAAP Operating Income / (Loss)</strong></td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">(-$8,000M)</td>
                    <td class="align-right">(-$2,135M)</td>
                    <td class="align-right">(-$693M)</td>
                    <td class="align-right">-4.3% (+8.4% in Q2)</td>
                </tr>
                <tr>
                    <td>&nbsp;&nbsp;&mdash; Non-Cash Fair Value Adjustment on Convertible Notes (ASC 825-10)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right" style="color: var(--accent-red);">(-$72,400M)</td>
                    <td class="align-right">-444.6%</td>
                </tr>
                <tr style="background: rgba(239, 68, 68, 0.1); font-weight: bold;">
                    <td><strong>GAAP Net Loss</strong></td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">(-$42,000M)</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right" style="color: var(--accent-red);">(-$80,748M)</td>
                    <td class="align-right">-495.8%</td>
                </tr>
                <tr style="background: rgba(16, 185, 129, 0.1); font-weight: bold;">
                    <td><strong>Operating Cash Flow (Net Cash Provided by Operating Activities)</strong></td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">&mdash;</td>
                    <td class="align-right">(-$1,500M)</td>
                    <td class="align-right" style="color: var(--accent-green);">+$3,929M</td>
                    <td class="align-right">+24.1% OCF Margin</td>
                </tr>
            </tbody>
        </table>

        <div class="callout warning">
            <h4>Why Both the -$80.75B Net Loss and the 85.4% Gross Margin Are Accounting Illusions</h4>
            <p style="margin-bottom: 8px;">
                <strong>1. The Convertible Note Mirage (-$72.4B Non-Cash Charge):</strong> On Anthropic's June 30, 2026 balance sheet, total liabilities are $117.47B, of which <strong>$108.60B is convertible notes payable</strong>. However, the actual cash principal borrowed on those notes (primarily from Amazon in 2023–2024) is only <strong>$6.20B</strong> (a 17.5x fair-value multiplier). Because Anthropic elected the fair-value option (ASC 825-10), its surging private valuation forced a $72.4B paper loss through the income statement in H1 2026. Upon IPO closing, those notes convert into Class N non-voting common stock, leaving Anthropic with <strong>zero debt and $8.87B in routine operating liabilities</strong>.
            </p>
            <p>
                <strong>2. The Pre-Training R&amp;D Classification Mirage (85.4% vs. 45.1% Margin):</strong> Bulls highlight that direct inference Cost of Revenue is only $2.38B on $16.29B of H1 revenue (an 85.4% gross margin). But Anthropic books <strong>$6.57B of pre-training and research compute inside R&amp;D ($9.74B total R&amp;D)</strong>. Unlike traditional enterprise software that amortizes over a decade, frontier LLM weights decay economically in <strong>9 to 15 months</strong>. Pre-training the next Claude iteration is mandatory maintenance COGS required to defend its customer base. Including total compute ($8.95B), true gross margin is <strong>45.1%</strong>.
            </p>
        </div>
    </div>

    <!-- SECTION 2: THE $688.6B TAKE-OR-PAY COMPUTE GUILLOTINE -->
    <div class="section">
        <h2>⚠️ 2. Feasibility Audit: The $587B–$688.6B Off-Balance-Sheet Compute Guillotine</h2>
        <p class="desc">
            The most critical disclosure in the S-1 lies in the Commitments &amp; Contingencies and Subsequent Events footnotes. While Anthropic left the calendar-year payment schedule blank in the initial filing, aggregating the counterparty contracts reveals an unprecedented fixed-cost obligation.
        </p>

        <div class="chart-row">
            <div class="chart-container">
                <h3>Anthropic Liquidity Trajectory (2026–2030) vs. Mandatory Compute Floor ($B)</h3>
                <div class="chart-wrapper">
                    <canvas id="cashWaterfallChart"></canvas>
                </div>
            </div>
            <div class="chart-container">
                <h3>Counterparty Breakdown of $688.6B Infrastructure Commitments ($B)</h3>
                <div class="chart-wrapper">
                    <canvas id="counterpartyChart"></canvas>
                </div>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Infrastructure Counterparty</th>
                    <th class="align-right">Direct Cloud Minimum</th>
                    <th class="align-right">TPU / Hardware Leases</th>
                    <th class="align-right">Total Committed</th>
                    <th>Contract Window</th>
                    <th>Contractual Structure &amp; S-1 Footnote Details</th>
                </tr>
            </thead>
            <tbody>
                {"".join(f'''<tr>
                    <td><strong>{c["counterparty"]}</strong></td>
                    <td class="align-right">${c["direct_take_or_pay_cloud_billions"]:.1f}B</td>
                    <td class="align-right">${c["additional_tpu_capacity_midpoint_billions"]:.1f}B</td>
                    <td class="align-right" style="color: var(--accent-red); font-weight: 700;">${c["total_committed_billions"]:.1f}B</td>
                    <td>{c["window"]}</td>
                    <td>{c["contract_type"]}</td>
                </tr>''' for c in comm["counterparties"])}
                <tr style="background: rgba(239, 68, 68, 0.12); font-weight: bold;">
                    <td><strong>TOTAL GROSS INFRASTRUCTURE COMMITMENTS</strong></td>
                    <td class="align-right">$389.9B</td>
                    <td class="align-right">$298.7B</td>
                    <td class="align-right" style="color: var(--accent-red); font-size: 1.05rem;">$688.6B</td>
                    <td>2026 &ndash; 2034+</td>
                    <td>Baseline as of June 30, 2026: $265.6B purchase minimums + $321.4B uncommenced leases ($587.0B)</td>
                </tr>
            </tbody>
        </table>

        <div class="flow-grid">
            <div class="flow-step">
                <div class="step-tag">Risk Pillar 1</div>
                <h4>80% Variable Token Revenue vs. 100% Fixed Leases</h4>
                <p>80.2% of H1 revenue ($13.06B) comes from pay-as-you-go API token consumption, and ~25% of revenue is concentrated in just 5 top customers. Yet the $688.6B compute commitments are legally binding <em>"regardless of actual usage."</em></p>
            </div>
            <div class="flow-step">
                <div class="step-tag">Risk Pillar 2</div>
                <h4>The Blank Payment Schedule Omission</h4>
                <p>Anthropic left the annual 2026–2030 contractual obligations table blank in the initial S-1. Phasing $688.6B over 7–8 years implies mandatory compute outflows ramping from $22B (2026) to <strong>$86B (2028) and $115B/yr (2030)</strong>.</p>
            </div>
            <div class="flow-step">
                <div class="step-tag">Risk Pillar 3</div>
                <h4>Circular Hyperscaler Financing &amp; Channel Tax</h4>
                <p>48% of H1 revenue ($7.82B) was routed through AWS, Google Cloud, and Azure marketplaces, costing $3.81B in S&amp;M channel fees. Hyperscalers funded Anthropic's $131.7B cash pile only to recapture it via locked-in cloud leases and marketplace tolls.</p>
            </div>
            <div class="flow-step">
                <div class="step-tag">Risk Pillar 4</div>
                <h4>42.4% Hyperscaler Depreciation Transfer</h4>
                <p>In our macro model, the Big-4 hyperscalers face a $202.9B/yr AI carrying burden (D&amp;A + power). By 2028, Anthropic's $86B/yr take-or-pay floor absorbs <strong>42.4% of that entire burden</strong>—shifting CapEx risk onto Anthropic's balance sheet.</p>
            </div>
        </div>
    </div>

    <!-- SECTION 3: 2026-2030 SCENARIO WATERFALL -->
    <div class="section">
        <h2>🔮 3. Scenario Projections: Anthropic's Financial Position (2026–2030)</h2>
        <p class="desc">
            Starting from <strong>$131.7B in June 30, 2026 liquid reserves</strong> ($146.7B pro-forma including $15.0B net IPO proceeds), we model three probability-weighted paths for Anthropic's income statement, cash buffer, and public market valuation.
        </p>

        <table>
            <thead>
                <tr>
                    <th>Scenario &amp; Probability Weight</th>
                    <th class="align-right">2026E Rev</th>
                    <th class="align-right">2028E Rev</th>
                    <th class="align-right">2030E Rev</th>
                    <th class="align-right">2028E Compute Outflow</th>
                    <th class="align-right">2026–30 Deadweight Compute</th>
                    <th class="align-right">2029E Cash Reserve</th>
                    <th class="align-right">2028E Implied Market Cap</th>
                    <th class="align-right">Return vs. $1.5T IPO</th>
                </tr>
            </thead>
            <tbody>
                {"".join(f'''<tr>
                    <td><strong>{sc["label"]} ({sc["probability"]:.0%})</strong></td>
                    <td class="align-right">${sc["annual_projections"][0]["revenue_billions"]:.1f}B</td>
                    <td class="align-right"><strong>${sc["summary_metrics"]["revenue_2028_billions"]:.1f}B</strong></td>
                    <td class="align-right">${sc["annual_projections"][4]["revenue_billions"]:.1f}B</td>
                    <td class="align-right">${sc["annual_projections"][2]["actual_compute_outflow_billions"]:.1f}B</td>
                    <td class="align-right" style="color: var(--accent-orange);">${sc["summary_metrics"]["cumulative_deadweight_compute_2026_2030_billions"]:.1f}B</td>
                    <td class="align-right" style="color: var(--accent-blue); font-weight: 700;">${sc["summary_metrics"]["ending_liquidity_2029_billions"]:.1f}B</td>
                    <td class="align-right"><strong>${sc["summary_metrics"]["implied_2028_market_cap_billions"]:.1f}B</strong></td>
                    <td class="align-right" style="color: {"#10b981" if sc["summary_metrics"]["implied_return_vs_1_5t_ipo_pct"] >= 0 else "#ef4444"}; font-weight: 700;">{sc["summary_metrics"]["implied_return_vs_1_5t_ipo_pct"]:+.1%}</td>
                </tr>''' for sc in scenarios_out["scenarios"].values())}
                <tr style="background: rgba(168, 85, 247, 0.12); font-weight: bold;">
                    <td><strong>PROBABILITY-WEIGHTED EXPECTED VALUE (100%)</strong></td>
                    <td class="align-right">$39.0B</td>
                    <td class="align-right">$87.5B</td>
                    <td class="align-right">$131.6B</td>
                    <td class="align-right">$75.3B</td>
                    <td class="align-right" style="color: var(--accent-orange);">$114.7B</td>
                    <td class="align-right" style="color: var(--accent-blue); font-size: 1.02rem;">${scenarios_out["probability_weighted_summary"]["expected_2029_liquidity_billions"]:.1f}B</td>
                    <td class="align-right" style="font-size: 1.02rem;">${scenarios_out["probability_weighted_summary"]["expected_2028_market_cap_billions"]:.1f}B</td>
                    <td class="align-right" style="color: var(--accent-red); font-size: 1.02rem;">{scenarios_out["probability_weighted_summary"]["expected_return_vs_1_5t_ipo_pct"]:+.1%}</td>
                </tr>
            </tbody>
        </table>

        <!-- Year-by-Year Breakdown of the 50% Base Case -->
        <h3 style="font-size: 1.02rem; margin: 22px 0 8px 0; color: #38bdf8;">Deep-Dive: Base Case Year-by-Year Cash Flow &amp; Take-or-Pay Schedule (50% Probability)</h3>
        <table>
            <thead>
                <tr>
                    <th>Year</th>
                    <th class="align-right">Revenue</th>
                    <th class="align-right">Scheduled Take-or-Pay</th>
                    <th class="align-right">Effective Compute Floor</th>
                    <th class="align-right">Organic Compute Need</th>
                    <th class="align-right">Unutilized Deadweight</th>
                    <th class="align-right">Compute-Adj Gross Margin</th>
                    <th class="align-right">GAAP Operating Income</th>
                    <th class="align-right">Free Cash Flow (incl. Interest)</th>
                    <th class="align-right">Ending Cash &amp; Securities</th>
                </tr>
            </thead>
            <tbody>
                {"".join(f'''<tr>
                    <td><strong>{r["year"]}E</strong></td>
                    <td class="align-right">${r["revenue_billions"]:.1f}B</td>
                    <td class="align-right">${r["scheduled_take_or_pay_billions"]:.1f}B</td>
                    <td class="align-right">${r["effective_take_or_pay_floor_billions"]:.1f}B</td>
                    <td class="align-right">${r["organic_compute_demand_billions"]:.1f}B</td>
                    <td class="align-right" style="color: var(--accent-orange);">${r["unutilized_deadweight_compute_billions"]:.1f}B</td>
                    <td class="align-right">{r["compute_adjusted_gross_margin_pct"]:.1%}</td>
                    <td class="align-right" style="color: {"#10b981" if r["operating_income_billions"] >= 0 else "#ef4444"};">${r["operating_income_billions"]:+.1f}B</td>
                    <td class="align-right" style="color: {"#10b981" if r["free_cash_flow_billions"] >= 0 else "#ef4444"};">${r["free_cash_flow_billions"]:+.1f}B</td>
                    <td class="align-right" style="color: var(--accent-blue); font-weight: 700;">${r["ending_liquidity_billions"]:.1f}B</td>
                </tr>''' for r in base_proj)}
            </tbody>
        </table>
    </div>

    <!-- SECTION 4: MARKET LEANINGS & IPO VERDICT -->
    <div class="section">
        <h2>🧭 4. Late-October 2026 Market Leanings: What They Signal About Anthropic's Success</h2>
        <p class="desc">
            The public market's reaction since the S-1 dropped on October 26, 2026 reveals a sharp bifurcation between <strong>Anthropic the enterprise product company</strong> and <strong><code>ANT</code> the $1.5T–$2.0T IPO security</strong>.
        </p>

        <div class="tldr-grid">
            <div class="tldr-item" style="border-left: 3px solid var(--accent-orange);">
                <h3>1. Immediate Valuation Haircut ($2.0T &rarr; $1.5T)</h3>
                <p>Initial whisper targets of $2.0T implied <strong>43x Q2 annualized revenue ($46.2B)</strong> and <strong>96x annualized compute-adjusted gross profit ($20.8B)</strong>. Within 72 hours of the S-1 filing, institutional pushback over the $688.6B off-balance-sheet obligations compressed target talk toward $1.5T, with disciplined crossover books modeling fair value near <strong>$900B–$1.1T</strong>.</p>
            </div>
            <div class="tldr-item" style="border-left: 3px solid var(--accent-red);">
                <h3>2. Post-SpaceX Mega-IPO Indigestion</h3>
                <p>Following the summer 2026 SpaceX IPO and a volatile autumn tech tape driven by data-center ROI skepticism, asset managers lack idle cash to absorb another $1.5T listing. Funding an allocation in <code>ANT</code> requires institutional PMs to liquidate existing positions in Nvidia, Microsoft, and Meta—turning the IPO into a <strong>liquidity drain</strong> on the broader AI trade.</p>
            </div>
            <div class="tldr-item" style="border-left: 3px solid var(--accent-green);">
                <h3>3. Undisputed Enterprise Application Leader</h3>
                <p>Market leanings confirm Anthropic has won the high-margin enterprise coding and knowledge-work tier via <strong>Claude Code</strong> and <strong>Claude Cowork</strong> (11,900+ customers &gt;$100k/yr; 1,900+ &gt;$1M/yr; ~250 whales &gt;$10M/yr). Unlike dot-com vaporware, Anthropic will endure as a foundational enterprise software pillar.</p>
            </div>
            <div class="tldr-item" style="border-left: 3px solid var(--accent-purple);">
                <h3>4. The Cisco / Amazon 2000 Parallel</h3>
                <p>Great companies can be terrible IPO-price investments when priced at the apex of a capital cycle. Even if Anthropic more than doubles its revenue to $85B by 2028 (Base Case), multiple normalization (from ~32x run-rate rev to 8.5x) plus take-or-pay margin compression yields a <strong>-43.7% drawdown from a $1.5T IPO price</strong>.</p>
            </div>
        </div>
    </div>
</div>

<script>
    // Embedded Take-or-Pay Schedule ($ Billions)
    const takeOrPaySchedule = {{
        2026: 22.0,
        2027: 52.0,
        2028: 86.0,
        2029: 108.0,
        2030: 115.0
    }};
    const startingCashJune2026 = 131.7;

    function updateAnthropicSimulator() {{
        const rev2028 = parseFloat(document.getElementById('simRev2028Slider').value);
        const compPct = parseFloat(document.getElementById('simCompPctSlider').value) / 100.0;
        const reliefPct = parseFloat(document.getElementById('simReliefSlider').value) / 100.0;
        const evMult = parseFloat(document.getElementById('simMultSlider').value);
        const ipoProceeds = parseFloat(document.getElementById('simIpoSlider').value);

        document.getElementById('simRev2028Val').innerText = '$' + rev2028.toFixed(0) + 'B';
        document.getElementById('simCompPctVal').innerText = (compPct * 100).toFixed(0) + '%';
        document.getElementById('simReliefVal').innerText = (reliefPct * 100).toFixed(0) + '%';
        document.getElementById('simMultVal').innerText = evMult.toFixed(1) + 'x';
        document.getElementById('simIpoVal').innerText = '$' + ipoProceeds.toFixed(0) + 'B';

        // Construct smooth 2026-2030 revenue path anchored on 2026 ($39.5B) and user's 2028 target
        const revPath = {{
            2026: 39.5,
            2027: 39.5 + (rev2028 - 39.5) * 0.55,
            2028: rev2028,
            2029: rev2028 * 1.18,
            2030: rev2028 * 1.35
        }};

        let liquidity = startingCashJune2026 + ipoProceeds;
        let out2028Comp = 0;
        let out2028Deadweight = 0;
        let out2028AdjMargin = 0;
        let out2028OpMargin = 0;
        let cash2029 = 0;

        for (const yr of [2026, 2027, 2028, 2029, 2030]) {{
            const rev = revPath[yr];
            const sched = takeOrPaySchedule[yr];
            const effFloor = (yr >= 2028) ? sched * (1.0 - reliefPct) : sched;
            const organicComp = rev * compPct;
            const actualComp = Math.max(effFloor, organicComp);
            const deadweight = Math.max(0.0, effFloor - organicComp);

            const adjGrossProfit = rev - actualComp;
            const adjGrossMargin = adjGrossProfit / rev;
            const nonCompOpex = Math.max(10.0, rev * 0.28);
            const opInc = adjGrossProfit - nonCompOpex;
            const opMargin = opInc / rev;
            const interestInc = Math.max(0.0, liquidity * 0.035);
            const fcf = opInc + interestInc;

            if (yr === 2026) {{
                liquidity = Math.max(0.0, liquidity + fcf * 0.5);
            }} else {{
                liquidity = Math.max(0.0, liquidity + fcf);
            }}

            if (yr === 2028) {{
                out2028Comp = actualComp;
                out2028Deadweight = deadweight;
                out2028AdjMargin = adjGrossMargin;
                out2028OpMargin = opMargin;
            }}
            if (yr === 2029) {{
                cash2029 = liquidity;
            }}
        }}

        const impliedMcap2028 = (rev2028 * evMult) + cash2029;
        const retVsIpo = (impliedMcap2028 - 1500.0) / 1500.0;

        document.getElementById('outComp2028').innerText = '$' + out2028Comp.toFixed(1) + 'B';
        document.getElementById('outDeadweight2028').innerText = 'Unutilized penalty: $' + out2028Deadweight.toFixed(1) + 'B in 2028';
        document.getElementById('outAdjMargin2028').innerText = (out2028AdjMargin * 100).toFixed(1) + '%';
        document.getElementById('outOpMargin2028').innerText = 'GAAP Operating Margin: ' + (out2028OpMargin * 100).toFixed(1) + '%';
        document.getElementById('outCash2029').innerText = '$' + cash2029.toFixed(1) + 'B';
        document.getElementById('outSolvencyTag').innerText = cash2029 > 140 ? 'SELF-FUNDING FORTRESS' : (cash2029 > 35 ? 'SOLVENT (Cash Buffer Absorbs Lease Deficit)' : 'DISTRESS: Lease Renegotiation Required');
        document.getElementById('outMcap2028').innerText = '$' + impliedMcap2028.toFixed(1) + 'B';
        document.getElementById('outMcap2028').className = 'value ' + (retVsIpo >= 0 ? 'green' : 'red');

        const sign = retVsIpo >= 0 ? '+' : '';
        const retEl = document.getElementById('outReturnVsIpo');
        retEl.innerText = sign + (retVsIpo * 100).toFixed(1) + '% vs. $1.5T IPO Valuation';
        retEl.style.color = retVsIpo >= 0 ? '#10b981' : '#ef4444';
    }}

    document.getElementById('simRev2028Slider').addEventListener('input', updateAnthropicSimulator);
    document.getElementById('simCompPctSlider').addEventListener('input', updateAnthropicSimulator);
    document.getElementById('simReliefSlider').addEventListener('input', updateAnthropicSimulator);
    document.getElementById('simMultSlider').addEventListener('input', updateAnthropicSimulator);
    document.getElementById('simIpoSlider').addEventListener('input', updateAnthropicSimulator);

    window.addEventListener('DOMContentLoaded', () => {{
        updateAnthropicSimulator();

        // Chart 1: Quarterly Revenue Trajectory
        new Chart(document.getElementById('quarterlyTrajectoryChart'), {{
            type: 'bar',
            data: {{
                labels: ['Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026', 'Q2 2026'],
                datasets: [
                    {{
                        label: 'Quarterly Revenue ($ Millions)',
                        data: [376, 787, 1382, 2040, 4731, 11555],
                        backgroundColor: ['#38bdf8', '#38bdf8', '#38bdf8', '#38bdf8', '#818cf8', '#10b981'],
                        borderRadius: 4
                    }}
                ]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }},
                    tooltip: {{
                        callbacks: {{
                            label: function(ctx) {{ return 'Revenue: $' + ctx.parsed.y.toLocaleString() + 'M'; }}
                        }}
                    }}
                }},
                scales: {{
                    y: {{
                        grid: {{ color: '#2e3a52' }},
                        ticks: {{ color: '#94a3b8', callback: function(v) {{ return '$' + (v / 1000).toFixed(0) + 'B'; }} }}
                    }},
                    x: {{ ticks: {{ color: '#94a3b8' }} }}
                }}
            }}
        }});

        // Chart 2: Gross Margin Illusion Waterfall
        new Chart(document.getElementById('marginIllusionChart'), {{
            type: 'bar',
            data: {{
                labels: [
                    'Accounting Gross Margin (85.4%)',
                    'True Compute-Adjusted GM (45.1%)',
                    'Post-Marketplace S&M Margin (21.7%)',
                    'H1 2026 GAAP Operating Margin (-4.3%)',
                    'Q2 2026 GAAP Operating Margin (+8.4%)'
                ],
                datasets: [{{
                    label: '% of Revenue',
                    data: [85.4, 45.1, 21.7, -4.3, 8.4],
                    backgroundColor: ['#38bdf8', '#f97316', '#a855f7', '#ef4444', '#10b981'],
                    borderRadius: 4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{ legend: {{ display: false }} }},
                scales: {{
                    y: {{
                        min: -15,
                        max: 100,
                        grid: {{ color: '#2e3a52' }},
                        ticks: {{ color: '#94a3b8', callback: function(v) {{ return v + '%'; }} }}
                    }},
                    x: {{ ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }} }}
                }}
            }}
        }});

        // Chart 3: Cash Fortress vs Mandatory Compute Outflow
        new Chart(document.getElementById('cashWaterfallChart'), {{
            type: 'line',
            data: {{
                labels: ['2026E', '2027E', '2028E', '2029E', '2030E'],
                datasets: [
                    {{
                        label: 'Bull Case Cash Reserve ($B)',
                        data: {[r["ending_liquidity_billions"] for r in bull_proj]},
                        borderColor: '#10b981',
                        borderWidth: 2.5,
                        pointRadius: 3,
                        fill: false
                    }},
                    {{
                        label: 'Base Case Cash Reserve ($B)',
                        data: {[r["ending_liquidity_billions"] for r in base_proj]},
                        borderColor: '#38bdf8',
                        borderWidth: 3.5,
                        pointRadius: 4,
                        fill: false
                    }},
                    {{
                        label: 'Bear Case Cash Reserve ($B)',
                        data: {[r["ending_liquidity_billions"] for r in bear_proj]},
                        borderColor: '#ef4444',
                        borderWidth: 2.5,
                        pointRadius: 3,
                        fill: false
                    }},
                    {{
                        label: 'Scheduled Take-or-Pay Compute Floor ($B/yr)',
                        data: [22.0, 52.0, 86.0, 108.0, 115.0],
                        borderColor: '#f97316',
                        borderDash: [5, 5],
                        borderWidth: 2.5,
                        pointRadius: 3,
                        fill: false
                    }}
                ]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ position: 'bottom', labels: {{ color: '#94a3b8', font: {{ size: 10 }}, boxWidth: 18 }} }}
                }},
                scales: {{
                    y: {{
                        grid: {{ color: '#2e3a52' }},
                        ticks: {{ color: '#94a3b8', callback: function(v) {{ return '$' + v + 'B'; }} }}
                    }},
                    x: {{ ticks: {{ color: '#94a3b8' }} }}
                }}
            }}
        }});

        // Chart 4: Counterparty Commitments Breakdown
        new Chart(document.getElementById('counterpartyChart'), {{
            type: 'bar',
            data: {{
                labels: [
                    'Google Cloud + TPUs ($252.0B)',
                    'Broadcom / Apollo ($161.2B)',
                    'SpaceX xAI Infra ($120.5B)',
                    'Amazon AWS ($110.0B)',
                    'Microsoft Azure ($44.9B)'
                ],
                datasets: [{{
                    label: 'Committed Spend ($ Billions)',
                    data: [252.0, 161.2, 120.5, 110.0, 44.9],
                    backgroundColor: ['#38bdf8', '#a855f7', '#f97316', '#eab308', '#10b981'],
                    borderRadius: 4
                }}]
            }},
            options: {{
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{ legend: {{ display: false }} }},
                scales: {{
                    x: {{
                        grid: {{ color: '#2e3a52' }},
                        ticks: {{ color: '#94a3b8', callback: function(v) {{ return '$' + v + 'B'; }} }}
                    }},
                    y: {{ ticks: {{ color: '#94a3b8' }} }}
                }}
            }}
        }});
    }});
</script>

</body>
</html>
"""

    # Guardrail: guarantee zero backslashes in the rendered HTML output
    assert "\\" not in html_content, "Found unexpected backslash in HTML content!"

    docs_out = SRC_DIR.parent.parent / "docs" / "anthropic_s1_evaluation.html"
    src_out = SRC_DIR / "anthropic_s1_evaluation.html"

    for p in [docs_out, src_out]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(html_content)

    print(f"Generated clean, zero-backslash Anthropic S-1 HTML evaluation at:\n- {docs_out}\n- {src_out}")


if __name__ == "__main__":
    generate_anthropic_s1_html()
