"""
S&P 500 Cohort Valuation & Crash Waterfall Engine
Part of the AI Bubble Burst & Financial Transmission Project.

@para-doc #csa-sp500-waterfall
Binds to spec-ai-bubble-economic-model.md §2.4 (S&P 500 Valuation & Crash Waterfall Engine).
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List


class SP500ValuationModel:
    """
    First-principles stock market valuation engine modeling the S&P 500 crash
    across four distinct equity cohorts following an AI infrastructure CapEx bust.
    """

    def __init__(self, data_dir: Optional[Path] = None):
        if data_dir is None:
            data_dir = Path(__file__).resolve().parent.parent / "data"
        self.data_dir = data_dir
        self.cohort_data = self._load_json(self.data_dir / "sp500_cohorts.json")
        self.benchmark = self.cohort_data["index_benchmark"]
        self.cohorts = self.cohort_data["cohorts"]

    def _load_json(self, path: Path) -> Dict[str, Any]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def simulate_crash(
        self,
        capex_cut_pct: float = 0.45,
        multiple_derate_severity: float = 0.75,
        macro_wealth_drag_pct: float = 0.08,
        bank_credit_drag_pct: float = 0.05,
    ) -> Dict[str, Any]:
        """
        Simulates constituent earnings shock, multiple compression, and peak-to-trough
        index drawdown across all four S&P 500 cohorts.

        :param capex_cut_pct: Hyperscaler capital expenditure contraction (e.g. 0.45 = 45% cut).
        :param multiple_derate_severity: 0.0 (no multiple change) to 1.0 (full trough multiple de-rating).
        :param macro_wealth_drag_pct: Wealth effect hit on cyclical earnings from lost market cap.
        :param bank_credit_drag_pct: Earnings reduction in broader economy due to bank lending contraction.
        :return: Detailed cohort-level results, weighted index return, and stressed index level.
        """
        cohort_results = []
        aggregate_drawdown = 0.0
        weighted_new_eps = 0.0
        weighted_new_pe = 0.0

        base_level = self.benchmark["base_level"]
        base_eps = self.benchmark["base_aggregate_eps"]

        for c in self.cohorts:
            c_id = c["id"]
            weight = c["index_weight"]
            base_pe = c["base_forward_pe"]
            trough_pe = c["trough_pe"]

            # Calculate compressed P/E multiple
            target_pe = base_pe - (multiple_derate_severity * (base_pe - trough_pe))
            pe_compression_pct = (target_pe / base_pe) - 1.0

            # Calculate Cohort-specific EPS impairment
            if c_id == "cohort_1_silicon_enablers":
                # Semiconductor bullwhip: revenue drop = capex_cut * 1.35
                rev_drop = min(0.75, capex_cut_pct * c["operating_leverage_multiplier"])
                # Operating leverage with high fixed costs expands the EPS drop
                eps_impact = -min(0.78, rev_drop * 1.25)

            elif c_id == "cohort_2_hyperscalers":
                # Margin compression from D&A on past builds + cloud deceleration
                margin_drop_bps = (capex_cut_pct / 0.10) * c["margin_compression_bps_per_10pct_capex_cut"]
                margin_drag = margin_drop_bps / 10000.0 / c["baseline_operating_margin"]
                # Additional asset impairment write-down
                write_down_drag = 0.08 * (capex_cut_pct / 0.40)
                eps_impact = -min(0.45, margin_drag + write_down_drag)

            elif c_id == "cohort_3_power_infrastructure":
                # Utility & data center REIT growth multiple vanishes, contracts renegotiated
                eps_impact = -min(0.35, (capex_cut_pct / 0.10) * c["eps_haircut_per_10pct_capex_cut"])

            elif c_id == "cohort_4_broader_market":
                # Macro contagion: negative wealth effect + corporate IT freeze + bank credit pullback
                total_macro_drag = macro_wealth_drag_pct + bank_credit_drag_pct
                eps_impact = -min(0.25, total_macro_drag)

            else:
                eps_impact = 0.0

            # Price Change formula: (1 + EPS_impact) * (PE_new / PE_base) - 1
            price_change = ((1.0 + eps_impact) * (target_pe / base_pe)) - 1.0
            cohort_contribution = weight * price_change
            aggregate_drawdown += cohort_contribution

            cohort_results.append(
                {
                    "id": c_id,
                    "name": c["name"],
                    "index_weight": weight,
                    "key_constituents": c["key_constituents"],
                    "base_forward_pe": base_pe,
                    "stressed_forward_pe": round(target_pe, 2),
                    "pe_compression_pct": round(pe_compression_pct, 4),
                    "eps_impairment_pct": round(eps_impact, 4),
                    "price_change_pct": round(price_change, 4),
                    "index_drawdown_contribution_pct": round(cohort_contribution, 4),
                }
            )

        new_index_level = base_level * (1.0 + aggregate_drawdown)

        # Implied index aggregate EPS and P/E
        implied_aggregate_eps_change = sum(c["index_weight"] * c["eps_impairment_pct"] for c in cohort_results)
        stressed_aggregate_eps = base_eps * (1.0 + implied_aggregate_eps_change)
        stressed_aggregate_pe = new_index_level / stressed_aggregate_eps if stressed_aggregate_eps > 0 else 0.0

        return {
            "parameters": {
                "capex_cut_pct": capex_cut_pct,
                "multiple_derate_severity": multiple_derate_severity,
                "macro_wealth_drag_pct": macro_wealth_drag_pct,
                "bank_credit_drag_pct": bank_credit_drag_pct,
            },
            "index_summary": {
                "base_index_level": base_level,
                "stressed_index_level": round(new_index_level, 2),
                "peak_to_trough_drawdown_pct": round(aggregate_drawdown, 4),
                "base_aggregate_eps": base_eps,
                "stressed_aggregate_eps": round(stressed_aggregate_eps, 2),
                "aggregate_eps_growth_pct": round(implied_aggregate_eps_change, 4),
                "base_aggregate_pe": self.benchmark["base_aggregate_pe"],
                "stressed_aggregate_pe": round(stressed_aggregate_pe, 2),
            },
            "cohort_breakdown": cohort_results,
        }

    def run_predefined_crash_scenarios(self) -> Dict[str, Any]:
        """
        Runs three canonical crash scenarios:
        1. mild_disillusionment: 25% capex cut, 40% multiple de-rate, mild macro drag.
        2. base_bubble_burst: 45% capex cut, 75% multiple de-rate, moderate macro drag.
        3. systemic_liquidity_bust: 65% capex cut, 100% trough multiples, credit crunch.
        """
        scenarios = {
            "mild_disillusionment": {
                "capex_cut_pct": 0.25,
                "multiple_derate_severity": 0.40,
                "macro_wealth_drag_pct": 0.04,
                "bank_credit_drag_pct": 0.02,
            },
            "base_bubble_burst": {
                "capex_cut_pct": 0.45,
                "multiple_derate_severity": 0.75,
                "macro_wealth_drag_pct": 0.08,
                "bank_credit_drag_pct": 0.05,
            },
            "systemic_liquidity_bust": {
                "capex_cut_pct": 0.65,
                "multiple_derate_severity": 1.00,
                "macro_wealth_drag_pct": 0.14,
                "bank_credit_drag_pct": 0.10,
            },
        }

        return {k: self.simulate_crash(**v) for k, v in scenarios.items()}


if __name__ == "__main__":
    model = SP500ValuationModel()
    scenarios = model.run_predefined_crash_scenarios()
    for name, res in scenarios.items():
        summary = res["index_summary"]
        print(f"\n=== S&P 500 Scenario: {name} ===")
        print(f"Stressed Index Level: {summary['stressed_index_level']:,.1f} (from {summary['base_index_level']:,.1f})")
        print(f"Peak-to-Trough Drawdown: {summary['peak_to_trough_drawdown_pct']:.1%}")
        print(f"Aggregate EPS: ${summary['stressed_aggregate_eps']:.2f} ({summary['aggregate_eps_growth_pct']:.1%})")
        print(f"Aggregate P/E: {summary['stressed_aggregate_pe']:.1f}x (from {summary['base_aggregate_pe']:.1f}x)")
        print("Cohort Drawdown Breakdown:")
        for c in res["cohort_breakdown"]:
            print(f"  - {c['name']}: {c['price_change_pct']:.1%} (Contribution: {c['index_drawdown_contribution_pct']:.1%})")
