"""
Labor Demographic & CapEx Payback Deficit Model
Part of the AI Bubble Burst & Financial Transmission Project.

@para-doc #csa-labor-model
Binds to spec-ai-bubble-economic-model.md §2.1 (Labor Displacement & Wage Savings Engine).

@para-doc #csa-capex-deficit
Binds to spec-ai-bubble-economic-model.md §2.2 (CapEx Run-Rate & Payback Deficit Engine).
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List


class LaborCapexModel:
    """
    First-principles quantitative model connecting white-collar labor displacement,
    wage savings, enterprise software revenue capture, and hyperscaler CapEx deficit.
    """

    def __init__(self, data_dir: Optional[Path] = None):
        if data_dir is None:
            data_dir = Path(__file__).resolve().parent.parent / "data"
        self.data_dir = data_dir
        self.occupations_data = self._load_json(self.data_dir / "bls_occupations.json")
        self.capex_data = self._load_json(self.data_dir / "hyperscaler_capex.json")

    def _load_json(self, path: Path) -> Dict[str, Any]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def compute_labor_savings(
        self, custom_displacements: Optional[Dict[str, Dict[str, float]]] = None
    ) -> Dict[str, Any]:
        """
        Computes labor displacement, payroll reductions, and gross wage savings
        across the 7 high-exposure occupational categories and 3 seniority tiers.

        :param custom_displacements: Optional mapping of occupation_id -> {tier: displacement_rate}
        :return: Detailed breakdown of displaced headcount and total wage savings.
        """
        total_headcount = 0
        total_payroll = 0.0
        total_displaced_workers = 0
        total_wage_savings = 0.0

        occupation_results = []

        for occ in self.occupations_data["occupations"]:
            occ_id = occ["id"]
            occ_headcount = occ["total_headcount"]
            total_headcount += occ_headcount

            occ_displaced = 0
            occ_savings = 0.0
            occ_payroll = 0.0

            tier_breakdown = {}

            for tier_name, tier_info in occ["tiers"].items():
                tier_headcount = occ_headcount * tier_info["share_of_headcount"]
                tier_loaded_cost = tier_info["fully_loaded_cost"]
                tier_payroll = tier_headcount * tier_loaded_cost
                occ_payroll += tier_payroll

                if custom_displacements and occ_id in custom_displacements:
                    disp_pct = custom_displacements[occ_id].get(
                        tier_name, tier_info["default_displacement_pct"]
                    )
                elif custom_displacements and "global" in custom_displacements:
                    disp_pct = custom_displacements["global"].get(
                        tier_name, tier_info["default_displacement_pct"]
                    )
                else:
                    disp_pct = tier_info["default_displacement_pct"]

                displaced = tier_headcount * disp_pct
                savings = displaced * tier_loaded_cost

                occ_displaced += displaced
                occ_savings += savings

                tier_breakdown[tier_name] = {
                    "headcount": tier_headcount,
                    "displacement_pct": disp_pct,
                    "displaced_workers": round(displaced),
                    "wage_savings": round(savings, 2),
                }

            total_payroll += occ_payroll
            total_displaced_workers += occ_displaced
            total_wage_savings += occ_savings

            occupation_results.append(
                {
                    "id": occ_id,
                    "title": occ["title"],
                    "total_headcount": occ_headcount,
                    "total_payroll": round(occ_payroll, 2),
                    "displaced_workers": round(occ_displaced),
                    "effective_displacement_pct": round(occ_displaced / occ_headcount, 4),
                    "wage_savings": round(occ_savings, 2),
                    "tiers": tier_breakdown,
                }
            )

        effective_macro_displacement = (
            total_displaced_workers / total_headcount if total_headcount > 0 else 0.0
        )

        return {
            "total_benchmark_headcount": total_headcount,
            "total_annual_payroll": round(total_payroll, 2),
            "total_displaced_workers": round(total_displaced_workers),
            "effective_displacement_pct": round(effective_macro_displacement, 4),
            "total_gross_wage_savings": round(total_wage_savings, 2),
            "occupations": occupation_results,
        }

    def compute_capex_deficit(
        self,
        year: str = "2026",
        useful_life_years: float = 4.0,
        power_cooling_ratio: float = 0.10,
        enterprise_capture_ratio: float = 0.18,
        custom_displacements: Optional[Dict[str, Dict[str, float]]] = None,
    ) -> Dict[str, Any]:
        """
        Calculates the Return on Invested Capital (ROIC) deficit comparing annual CapEx
        and depreciation against captured enterprise software revenue.
        """
        labor_summary = self.compute_labor_savings(custom_displacements)
        wage_savings = labor_summary["total_gross_wage_savings"]

        addressable_software_revenue = wage_savings * enterprise_capture_ratio

        capex_info = self.capex_data["historical_and_projected_capex"][year]
        big4_capex = capex_info["big4_total"]
        global_capex = capex_info["global_ai_capex"]

        hardware_share = self.capex_data["economic_assumptions"]["hardware_share_of_capex"]
        facilities_share = self.capex_data["economic_assumptions"]["facilities_share_of_capex"]

        # Hardware depreciates in useful_life_years (3-4 yrs); Facilities/shells over 15 yrs
        annual_depreciation_big4 = (
            (big4_capex * hardware_share / useful_life_years)
            + (big4_capex * facilities_share / 15.0)
        )
        annual_depreciation_global = (
            (global_capex * hardware_share / useful_life_years)
            + (global_capex * facilities_share / 15.0)
        )

        annual_power_cooling_big4 = big4_capex * power_cooling_ratio
        annual_power_cooling_global = global_capex * power_cooling_ratio

        total_annual_carrying_cost_big4 = annual_depreciation_big4 + annual_power_cooling_big4
        total_annual_carrying_cost_global = (
            annual_depreciation_global + annual_power_cooling_global
        )

        net_deficit_big4 = addressable_software_revenue - total_annual_carrying_cost_big4
        net_deficit_global = addressable_software_revenue - total_annual_carrying_cost_global

        roic_big4 = net_deficit_big4 / big4_capex if big4_capex > 0 else 0.0
        roic_global = net_deficit_global / global_capex if global_capex > 0 else 0.0

        return {
            "analysis_year": year,
            "big4_capex": big4_capex,
            "global_ai_capex": global_capex,
            "gross_wage_savings": round(wage_savings, 2),
            "enterprise_capture_ratio": enterprise_capture_ratio,
            "addressable_ai_software_revenue": round(addressable_software_revenue, 2),
            "depreciation_schedule": {
                "hardware_useful_life": useful_life_years,
                "annual_depreciation_big4": round(annual_depreciation_big4, 2),
                "annual_depreciation_global": round(annual_depreciation_global, 2),
            },
            "power_and_cooling_opex": {
                "ratio": power_cooling_ratio,
                "annual_opex_big4": round(annual_power_cooling_big4, 2),
                "annual_opex_global": round(annual_power_cooling_global, 2),
            },
            "total_annual_carrying_cost_big4": round(total_annual_carrying_cost_big4, 2),
            "total_annual_carrying_cost_global": round(total_annual_carrying_cost_global, 2),
            "net_annual_deficit_big4": round(net_deficit_big4, 2),
            "net_annual_deficit_global": round(net_deficit_global, 2),
            "roic_big4": round(roic_big4, 4),
            "roic_global": round(roic_global, 4),
            "subprime_mortgage_comparison": {
                "subprime_peak_2004_2007": self.capex_data["economic_assumptions"][
                    "subprime_mortgage_comparison"
                ]["subprime_peak_issuance_2004_2007_total"],
                "three_year_ai_capex": self.capex_data["economic_assumptions"][
                    "subprime_mortgage_comparison"
                ]["ai_capex_2024_2026_three_year_total"],
                "capex_to_subprime_ratio": round(
                    self.capex_data["economic_assumptions"][
                        "subprime_mortgage_comparison"
                    ]["ai_capex_2024_2026_three_year_total"]
                    / self.capex_data["economic_assumptions"][
                        "subprime_mortgage_comparison"
                    ]["subprime_peak_issuance_2004_2007_total"],
                    2,
                ),
            },
        }

    def run_predefined_scenarios(self) -> Dict[str, Any]:
        """
        Runs four canonical economic scenarios:
        1. tech_and_law_only: 20% junior/mid in tech & law only, 0% elsewhere.
        2. user_moderate_knowledge: ~20% junior, 10% mid across all 7 fields, 1% senior.
        3. conservative_stagnation: 10% junior, 3% mid across all 7 fields, 0% senior.
        4. aggressive_automation: 35% junior, 20% mid, 5% senior.
        """
        scenarios = {
            "tech_and_law_only": {
                "software_engineering": {"junior": 0.20, "mid": 0.15, "senior": 0.02},
                "legal_services": {"junior": 0.25, "mid": 0.12, "senior": 0.01},
                "finance_accounting": {"junior": 0.0, "mid": 0.0, "senior": 0.0},
                "customer_support": {"junior": 0.0, "mid": 0.0, "senior": 0.0},
                "marketing_creative": {"junior": 0.0, "mid": 0.0, "senior": 0.0},
                "consulting_analytics": {"junior": 0.0, "mid": 0.0, "senior": 0.0},
                "administrative_clerks": {"junior": 0.0, "mid": 0.0, "senior": 0.0},
            },
            "user_moderate_knowledge": {
                "global": {"junior": 0.22, "mid": 0.10, "senior": 0.015}
            },
            "conservative_stagnation": {
                "global": {"junior": 0.10, "mid": 0.04, "senior": 0.00}
            },
            "aggressive_automation": {
                "global": {"junior": 0.35, "mid": 0.20, "senior": 0.05}
            },
        }

        results = {}
        for sc_name, disp in scenarios.items():
            results[sc_name] = self.compute_capex_deficit(
                year="2026",
                useful_life_years=4.0,
                enterprise_capture_ratio=0.18,
                custom_displacements=disp,
            )

        return results


if __name__ == "__main__":
    model = LaborCapexModel()
    scenarios = model.run_predefined_scenarios()
    for name, res in scenarios.items():
        print(f"\n=== Scenario: {name} ===")
        print(f"Gross Wage Savings: ${res['gross_wage_savings']:,.0f}")
        print(f"Addressable Software Rev: ${res['addressable_ai_software_revenue']:,.0f}")
        print(f"Big4 Carrying Cost (D&A + Power): ${res['total_annual_carrying_cost_big4']:,.0f}")
        print(f"Net Deficit (Big4): ${res['net_annual_deficit_big4']:,.0f}")
        print(f"ROIC (Big4): {res['roic_big4']:.1%}")
