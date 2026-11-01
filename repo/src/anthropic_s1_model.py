"""
Anthropic S-1 Financial Feasibility, Take-or-Pay Compute Waterfall & Macro Reconciliation Model
Part of the AI Bubble Burst & Financial Transmission Project.

@para-doc #csa-anthropic-s1
Binds to spec-ai-bubble-economic-model.md §2.5 (Frontier Lab Micro-Foundations: Anthropic S-1 Take-or-Pay & Liquidity Stress-Test Engine).
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List

try:
    from labor_capex_model import LaborCapexModel
except ImportError:
    from .labor_capex_model import LaborCapexModel


class AnthropicS1Model:
    """
    First-principles financial model evaluating Anthropic, PBC's Form S-1 (filed Oct 26, 2026,
    ticker: ANT), reconciling GAAP vs. economic unit economics, stress-testing the $587B-$688.6B
    off-balance-sheet take-or-pay compute waterfall (2026-2030), and linking frontier lab revenue
    to the macroeconomic hyperscaler CapEx payback deficit.
    """

    def __init__(self, data_dir: Optional[Path] = None):
        if data_dir is None:
            data_dir = Path(__file__).resolve().parent.parent / "data"
        self.data_dir = data_dir
        self.s1_data = self._load_json(self.data_dir / "anthropic_s1_2026.json")

    def _load_json(self, path: Path) -> Dict[str, Any]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def reconcile_s1_unit_economics(self) -> Dict[str, Any]:
        """
        Reconciles Anthropic's H1 2026 GAAP income statement and balance sheet against
        true underlying economic unit margins and post-IPO pro-forma solvency.
        """
        h1_26 = self.s1_data["half_year_comparison_millions"]["H1_2026"]
        q2_26 = self.s1_data["quarterly_revenue_trajectory_millions"]["Q2_2026"]
        bs = self.s1_data["balance_sheet_june_30_2026_millions"]

        rev = h1_26["total_revenue"]
        inference_cogs = h1_26["functional_expense_breakdown_note8"]["cost_of_revenue_inference"]
        rd_pretraining = h1_26["functional_expense_breakdown_note8"][
            "research_and_development_pretraining"
        ]
        sm_expense = h1_26["functional_expense_breakdown_note8"]["sales_and_marketing"]
        total_compute = h1_26["nature_of_expense_breakdown"]["compute_and_infrastructure"]

        # 1. Gross Margin Reconciliation: Accounting (Inference only) vs. Economic (All Compute)
        accounting_gross_profit = rev - inference_cogs
        accounting_gross_margin = accounting_gross_profit / rev

        compute_adjusted_gross_profit = rev - total_compute
        compute_adjusted_gross_margin = compute_adjusted_gross_profit / rev

        # Estimated portion of R&D that is pure pre-training/research compute vs personnel
        implied_rd_compute = total_compute - inference_cogs

        # 2. Net Income Reconciliation: Stripping ASC 825-10 Fair-Value Convertible Note Distortion
        gaap_net_loss = h1_26["net_loss"]
        conv_note_fv_loss = h1_26["non_cash_convertible_note_fair_value_loss"]
        gaap_op_loss = h1_26["operating_loss"]
        op_cash_flow = h1_26["operating_cash_flow"]

        # 3. Balance Sheet Pro-Forma Conversion (Convertible Notes + Preferred -> Common Equity)
        pre_ipo_liabilities = bs["total_liabilities"]
        conv_notes_carrying = bs["convertible_notes_carrying_fair_value"]
        conv_notes_principal = bs["convertible_notes_actual_principal"]
        pro_forma_remaining_liabilities = pre_ipo_liabilities - conv_notes_carrying

        # 4. Cloud Marketplace Channel Tax Analysis
        marketplace_rev = rev * h1_26["cloud_marketplace_routed_share"]
        effective_sm_to_marketplace_ratio = sm_expense / marketplace_rev

        return {
            "h1_2026_revenue_millions": rev,
            "q2_2026_annualized_run_rate_millions": q2_26["annualized_revenue_run_rate"],
            "q2_2026_operating_income_millions": q2_26["operating_income"],
            "q2_2026_operating_margin_pct": round(
                q2_26["operating_income"] / q2_26["revenue"], 4
            ),
            "margin_reconciliation": {
                "inference_cost_of_revenue_millions": inference_cogs,
                "accounting_gross_profit_millions": round(accounting_gross_profit, 2),
                "accounting_gross_margin_pct": round(accounting_gross_margin, 4),
                "total_compute_and_infra_millions": total_compute,
                "implied_pretraining_research_compute_millions": round(implied_rd_compute, 2),
                "compute_adjusted_gross_profit_millions": round(
                    compute_adjusted_gross_profit, 2
                ),
                "compute_adjusted_gross_margin_pct": round(compute_adjusted_gross_margin, 4),
                "margin_illusion_spread_pct": round(
                    accounting_gross_margin - compute_adjusted_gross_margin, 4
                ),
            },
            "earnings_and_cash_reconciliation": {
                "gaap_net_loss_millions": gaap_net_loss,
                "non_cash_convertible_note_fv_loss_millions": conv_note_fv_loss,
                "gaap_operating_loss_millions": gaap_op_loss,
                "operating_cash_flow_millions": op_cash_flow,
                "convertible_note_principal_millions": conv_notes_principal,
                "convertible_note_carrying_value_millions": conv_notes_carrying,
                "fair_value_to_principal_multiplier": round(
                    conv_notes_carrying / conv_notes_principal, 2
                ),
            },
            "balance_sheet_fortress": {
                "liquid_reserves_millions": bs["total_liquid_reserves"],
                "pre_ipo_total_liabilities_millions": pre_ipo_liabilities,
                "pro_forma_post_conversion_liabilities_millions": round(
                    pro_forma_remaining_liabilities, 2
                ),
            },
            "channel_economics": {
                "marketplace_routed_revenue_millions": round(marketplace_rev, 2),
                "sales_and_marketing_millions": sm_expense,
                "sm_pct_of_total_revenue": round(sm_expense / rev, 4),
                "sm_to_marketplace_revenue_ratio": round(
                    effective_sm_to_marketplace_ratio, 4
                ),
            },
        }

    def get_commitments_summary(self) -> Dict[str, Any]:
        """
        Aggregates June 30, 2026 baseline commitments ($587.0B) and post-June 30 subsequent
        event counterparty obligations ($688.6B).
        """
        comm = self.s1_data["compute_and_infrastructure_commitments_billions"]
        baseline = comm["as_of_june_30_2026"]
        counterparties = comm["counterparty_breakdown_including_subsequent_events"]

        total_with_subsequent = sum(c["total_committed_billions"] for c in counterparties)
        return {
            "baseline_june_30_2026_billions": baseline["total_baseline_commitments"],
            "purchase_commitments_billions": baseline["non_cancelable_purchase_commitments"],
            "uncommenced_leases_billions": baseline[
                "uncommenced_compute_and_datacenter_leases"
            ],
            "total_including_subsequent_events_billions": round(total_with_subsequent, 2),
            "counterparties": counterparties,
            "annual_schedule_billions": comm["estimated_annual_take_or_pay_schedule_billions"],
        }

    def simulate_take_or_pay_waterfall(
        self,
        revenue_trajectory_billions: Dict[str, float],
        organic_compute_pct_of_rev: float = 0.48,
        non_compute_opex_pct_of_rev: float = 0.28,
        non_compute_fixed_opex_floor_billions: float = 8.0,
        lease_restructuring_relief_pct: float = 0.0,
        net_ipo_proceeds_billions: float = 15.0,
        terminal_ev_to_revenue_multiple: float = 10.0,
    ) -> Dict[str, Any]:
        """
        Simulates Anthropic's 2026-2030 cash flow, operating margins, and liquid reserves
        against its mandatory take-or-pay compute schedule.
        """
        schedule = self.s1_data["compute_and_infrastructure_commitments_billions"][
            "estimated_annual_take_or_pay_schedule_billions"
        ]
        starting_cash_billions = (
            self.s1_data["balance_sheet_june_30_2026_millions"]["total_liquid_reserves"]
            / 1000.0
        )

        # H1 2026 cash already includes H1 operations; add IPO proceeds in 2026
        current_liquidity = starting_cash_billions + net_ipo_proceeds_billions

        years = ["2026", "2027", "2028", "2029", "2030"]
        annual_results = []
        cumulative_fcf_2027_2030 = 0.0
        cumulative_deadweight_compute = 0.0

        for yr in years:
            rev = revenue_trajectory_billions[yr]
            scheduled_floor = schedule[yr]

            # Apply any emergency restructuring relief only from 2028 onward if stressed
            effective_floor = (
                scheduled_floor * (1.0 - lease_restructuring_relief_pct)
                if yr in ("2028", "2029", "2030")
                else scheduled_floor
            )

            organic_compute = rev * organic_compute_pct_of_rev
            actual_compute_outflow = max(effective_floor, organic_compute)
            unutilized_deadweight = max(0.0, effective_floor - organic_compute)

            compute_adj_gross_profit = rev - actual_compute_outflow
            compute_adj_gross_margin = compute_adj_gross_profit / rev if rev > 0 else 0.0

            non_compute_opex = max(
                non_compute_fixed_opex_floor_billions, rev * non_compute_opex_pct_of_rev
            )
            operating_income = compute_adj_gross_profit - non_compute_opex
            operating_margin = operating_income / rev if rev > 0 else 0.0

            # Interest income on cash (~3.5% yield) helps buffer FCF slightly
            interest_income = max(0.0, current_liquidity * 0.035)
            fcf = operating_income + interest_income

            if yr == "2026":
                # Only H2 2026 incremental FCF affects June 30, 2026 cash balance
                h2_incremental_fcf = fcf * 0.5
                current_liquidity = max(0.0, current_liquidity + h2_incremental_fcf)
            else:
                current_liquidity = max(0.0, current_liquidity + fcf)
                cumulative_fcf_2027_2030 += fcf

            cumulative_deadweight_compute += unutilized_deadweight

            annual_results.append(
                {
                    "year": yr,
                    "revenue_billions": round(rev, 2),
                    "scheduled_take_or_pay_billions": round(scheduled_floor, 2),
                    "effective_take_or_pay_floor_billions": round(effective_floor, 2),
                    "organic_compute_demand_billions": round(organic_compute, 2),
                    "actual_compute_outflow_billions": round(actual_compute_outflow, 2),
                    "unutilized_deadweight_compute_billions": round(
                        unutilized_deadweight, 2
                    ),
                    "compute_adjusted_gross_profit_billions": round(
                        compute_adj_gross_profit, 2
                    ),
                    "compute_adjusted_gross_margin_pct": round(
                        compute_adj_gross_margin, 4
                    ),
                    "non_compute_opex_billions": round(non_compute_opex, 2),
                    "operating_income_billions": round(operating_income, 2),
                    "operating_margin_pct": round(operating_margin, 4),
                    "free_cash_flow_billions": round(fcf, 2),
                    "ending_liquidity_billions": round(current_liquidity, 2),
                }
            )

        # 2028/2029 valuation check
        rev_2028 = revenue_trajectory_billions["2028"]
        end_liq_2029 = [r for r in annual_results if r["year"] == "2029"][0][
            "ending_liquidity_billions"
        ]
        implied_ev_2028 = rev_2028 * terminal_ev_to_revenue_multiple
        implied_market_cap_2028 = implied_ev_2028 + end_liq_2029
        ipo_baseline_val = self.s1_data["filing_metadata"][
            "revised_market_consensus_valuation_billions"
        ]
        return_vs_ipo_pct = (implied_market_cap_2028 - ipo_baseline_val) / ipo_baseline_val

        return {
            "starting_liquidity_june_2026_billions": starting_cash_billions,
            "net_ipo_proceeds_billions": net_ipo_proceeds_billions,
            "pro_forma_2026_starting_cash_billions": round(
                starting_cash_billions + net_ipo_proceeds_billions, 2
            ),
            "annual_projections": annual_results,
            "summary_metrics": {
                "revenue_2028_billions": round(rev_2028, 2),
                "ending_liquidity_2029_billions": round(end_liq_2029, 2),
                "ending_liquidity_2030_billions": round(current_liquidity, 2),
                "cumulative_fcf_2027_2030_billions": round(cumulative_fcf_2027_2030, 2),
                "cumulative_deadweight_compute_2026_2030_billions": round(
                    cumulative_deadweight_compute, 2
                ),
                "implied_2028_market_cap_billions": round(implied_market_cap_2028, 2),
                "ipo_reference_valuation_billions": ipo_baseline_val,
                "implied_return_vs_1_5t_ipo_pct": round(return_vs_ipo_pct, 4),
                "solvency_status": (
                    "SOLVENT_SELF_FUNDING"
                    if cumulative_fcf_2027_2030 > 0
                    else (
                        "SOLVENT_CASH_BUFFER_BURN"
                        if current_liquidity > 20.0
                        else "DISTRESS_RESTRUCTURING_REQUIRED"
                    )
                ),
            },
        }

    def run_predefined_s1_scenarios(self) -> Dict[str, Any]:
        """
        Runs the three canonical post-IPO trajectories for Anthropic (2026-2030):
        1. agentic_singularity_bull: 20% probability — NRR stays elevated, senior knowledge work automated.
        2. rational_enterprise_base: 50% probability — NRR normalizes to 115-125%, junior/mid ceiling reached.
        3. ai_bubble_burst_bear: 30% probability — Token price deflation + enterprise ROI freeze hits take-or-pay wall.
        """
        scenarios_config = {
            "agentic_singularity_bull": {
                "label": "Bull Case: Agentic Singularity",
                "probability": 0.20,
                "revenue_trajectory_billions": {
                    "2026": 42.0,
                    "2027": 95.0,
                    "2028": 165.0,
                    "2029": 230.0,
                    "2030": 300.0,
                },
                "organic_compute_pct_of_rev": 0.46,
                "non_compute_opex_pct_of_rev": 0.24,
                "non_compute_fixed_opex_floor_billions": 10.0,
                "lease_restructuring_relief_pct": 0.0,
                "terminal_ev_to_revenue_multiple": 14.0,
            },
            "rational_enterprise_base": {
                "label": "Base Case: Rational Enterprise Plateau",
                "probability": 0.50,
                "revenue_trajectory_billions": {
                    "2026": 39.5,
                    "2027": 64.0,
                    "2028": 85.0,
                    "2029": 102.0,
                    "2030": 118.0,
                },
                "organic_compute_pct_of_rev": 0.50,
                "non_compute_opex_pct_of_rev": 0.28,
                "non_compute_fixed_opex_floor_billions": 11.0,
                "lease_restructuring_relief_pct": 0.10,
                "terminal_ev_to_revenue_multiple": 8.5,
            },
            "ai_bubble_burst_bear": {
                "label": "Bear Case: AI Bubble Burst & Token Deflation",
                "probability": 0.30,
                "revenue_trajectory_billions": {
                    "2026": 36.0,
                    "2027": 44.0,
                    "2028": 40.0,
                    "2029": 38.0,
                    "2030": 42.0,
                },
                "organic_compute_pct_of_rev": 0.52,
                "non_compute_opex_pct_of_rev": 0.30,
                "non_compute_fixed_opex_floor_billions": 10.0,
                "lease_restructuring_relief_pct": 0.25,
                "terminal_ev_to_revenue_multiple": 4.5,
            },
        }

        results = {}
        for key, cfg in scenarios_config.items():
            sim = self.simulate_take_or_pay_waterfall(
                revenue_trajectory_billions=cfg["revenue_trajectory_billions"],
                organic_compute_pct_of_rev=cfg["organic_compute_pct_of_rev"],
                non_compute_opex_pct_of_rev=cfg["non_compute_opex_pct_of_rev"],
                non_compute_fixed_opex_floor_billions=cfg[
                    "non_compute_fixed_opex_floor_billions"
                ],
                lease_restructuring_relief_pct=cfg["lease_restructuring_relief_pct"],
                terminal_ev_to_revenue_multiple=cfg["terminal_ev_to_revenue_multiple"],
            )
            sim["label"] = cfg["label"]
            sim["probability"] = cfg["probability"]
            results[key] = sim

        # Compute probability-weighted expected 2028 Market Cap & 2029 Liquidity
        expected_mcap_2028 = sum(
            res["probability"] * res["summary_metrics"]["implied_2028_market_cap_billions"]
            for res in results.values()
        )
        expected_liq_2029 = sum(
            res["probability"] * res["summary_metrics"]["ending_liquidity_2029_billions"]
            for res in results.values()
        )

        return {
            "scenarios": results,
            "probability_weighted_summary": {
                "expected_2028_market_cap_billions": round(expected_mcap_2028, 2),
                "expected_2029_liquidity_billions": round(expected_liq_2029, 2),
                "expected_return_vs_1_5t_ipo_pct": round(
                    (expected_mcap_2028 - 1500.0) / 1500.0, 4
                ),
            },
        }

    def reconcile_with_macro_bubble_model(
        self, labor_model: Optional[LaborCapexModel] = None
    ) -> Dict[str, Any]:
        """
        Connects Anthropic's S-1 revenue and $688.6B compute commitments to the macroeconomic
        Labor Displacement and Hyperscaler CapEx Payback Deficit model.
        """
        if labor_model is None:
            labor_model = LaborCapexModel(data_dir=self.data_dir)

        macro_scenarios = labor_model.run_predefined_scenarios()
        base_macro = macro_scenarios["user_moderate_knowledge"]
        aggr_macro = macro_scenarios["aggressive_automation"]

        # Software engineering specific savings in base case
        labor_detail = labor_model.compute_labor_savings(
            {"global": {"junior": 0.22, "mid": 0.10, "senior": 0.015}}
        )
        swe_occ = [
            o for o in labor_detail["occupations"] if o["id"] == "software_engineering"
        ][0]
        swe_wage_savings_billions = swe_occ["wage_savings"] / 1e9

        ant_q2_run_rate_billions = (
            self.s1_data["quarterly_revenue_trajectory_millions"]["Q2_2026"][
                "annualized_revenue_run_rate"
            ]
            / 1000.0
        )
        base_addressable_sw_billions = (
            base_macro["addressable_ai_software_revenue"] / 1e9
        )
        aggr_addressable_sw_billions = (
            aggr_macro["addressable_ai_software_revenue"] / 1e9
        )
        big4_carrying_cost_billions = (
            base_macro["total_annual_carrying_cost_big4"] / 1e9
        )

        # Hyperscaler risk transfer calculation:
        # Anthropic's 2028 scheduled take-or-pay ($86B) as a share of Big-4 annual carrying cost ($202.9B)
        ant_2028_take_or_pay = self.s1_data[
            "compute_and_infrastructure_commitments_billions"
        ]["estimated_annual_take_or_pay_schedule_billions"]["2028"]
        hyperscaler_carrying_offset_share = (
            ant_2028_take_or_pay / big4_carrying_cost_billions
        )

        return {
            "anthropic_q2_2026_run_rate_billions": round(ant_q2_run_rate_billions, 2),
            "us_swe_gross_wage_savings_billions": round(swe_wage_savings_billions, 2),
            "macro_base_addressable_ai_software_billions": round(
                base_addressable_sw_billions, 2
            ),
            "macro_aggressive_addressable_ai_software_billions": round(
                aggr_addressable_sw_billions, 2
            ),
            "anthropic_share_of_base_macro_pool_pct": round(
                ant_q2_run_rate_billions / base_addressable_sw_billions, 4
            ),
            "anthropic_share_of_aggressive_macro_pool_pct": round(
                ant_q2_run_rate_billions / aggr_addressable_sw_billions, 4
            ),
            "big4_2026_annual_carrying_cost_billions": round(
                big4_carrying_cost_billions, 2
            ),
            "anthropic_2028_scheduled_take_or_pay_billions": ant_2028_take_or_pay,
            "hyperscaler_depreciation_transferred_to_anthropic_pct": round(
                hyperscaler_carrying_offset_share, 4
            ),
        }


if __name__ == "__main__":
    model = AnthropicS1Model()
    recon = model.reconcile_s1_unit_economics()
    print("=== Anthropic S-1 Unit Economics Reconciliation ===")
    print(
        f"H1 2026 Revenue: ${recon['h1_2026_revenue_millions']:,.0f}M "
        f"(Q2 Run-Rate: ${recon['q2_2026_annualized_run_rate_millions']:,.0f}M)"
    )
    print(
        f"Accounting Gross Margin: {recon['margin_reconciliation']['accounting_gross_margin_pct']:.1%} vs. "
        f"Compute-Adjusted Gross Margin: {recon['margin_reconciliation']['compute_adjusted_gross_margin_pct']:.1%}"
    )

    sim_out = model.run_predefined_s1_scenarios()
    for name, sc in sim_out["scenarios"].items():
        sm = sc["summary_metrics"]
        print(
            f"\n[{sc['label']}] 2028 Rev: ${sm['revenue_2028_billions']}B | "
            f"2029 Cash: ${sm['ending_liquidity_2029_billions']}B | "
            f"2028 Implied MCap: ${sm['implied_2028_market_cap_billions']}B ({sm['implied_return_vs_1_5t_ipo_pct']:+.1%})"
        )
