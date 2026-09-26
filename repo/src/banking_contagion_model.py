"""
Banking & Shadow Credit Transmission Engine
Part of the AI Bubble Burst & Financial Transmission Project.

@para-doc #csa-banking-pipeline
Binds to spec-ai-bubble-economic-model.md §2.3 (Banking & Shadow Credit Transmission Pipeline).
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional


class BankingContagionModel:
    """
    Simulates the transmission of AI infrastructure debt defaults and mark-to-market
    shocks into regulated commercial banks and the shadow banking system.
    """

    def __init__(self, data_dir: Optional[Path] = None):
        if data_dir is None:
            data_dir = Path(__file__).resolve().parent.parent / "data"
        self.data_dir = data_dir
        self.debt_data = self._load_json(self.data_dir / "debt_facilities.json")
        self.channels = self.debt_data["channels"]
        self.bank_baseline = self.debt_data["commercial_banking_system_baseline"]

    def _load_json(self, path: Path) -> Dict[str, Any]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def simulate_stress_scenario(
        self,
        gpu_hardware_haircut_pct: float = 0.60,
        ai_contract_default_pct: float = 0.45,
        warehouse_debt_markdown_pct: float = 0.25,
        cre_datacenter_default_pct: float = 0.12,
        utility_spread_widening_bps: float = 200.0,
    ) -> Dict[str, Any]:
        """
        Executes a credit stress test across all five financial debt channels.

        :param gpu_hardware_haircut_pct: Depreciation/haircut on GPU collateral (e.g. 0.60 = 60% loss in resale value).
        :param ai_contract_default_pct: Proportion of AI startups/labs defaulting on take-or-pay compute contracts.
        :param warehouse_debt_markdown_pct: Mark-to-market haircut on hung bridge loans on bank balance sheets.
        :param cre_datacenter_default_pct: Default rate on data center commercial mortgages.
        :param utility_spread_widening_bps: Credit spread widening on utility/grid debt (in basis points).
        :return: Detailed breakdown of losses by channel, bank capital impact, and credit contraction.
        """
        channel_results = {}
        total_system_losses = 0.0
        total_bank_losses = 0.0
        total_shadow_bank_losses = 0.0

        # Channel 1: Neo-Cloud GPU Debt ($68B)
        ch1 = self.channels["channel_1_gpu_neocloud_debt"]
        principal_1 = ch1["total_principal"]
        original_ltv = ch1["original_ltv"]
        collateral_recovery_rate = max(0.15, (1.0 - gpu_hardware_haircut_pct) / original_ltv)
        lgd_1 = max(0.0, 1.0 - collateral_recovery_rate)
        loss_1_total = principal_1 * ai_contract_default_pct * lgd_1
        loss_1_bank = loss_1_total * ch1["bank_direct_exposure_share"]
        loss_1_shadow = loss_1_total * ch1["shadow_bank_private_credit_share"]

        channel_results["channel_1_gpu_neocloud_debt"] = {
            "name": ch1["name"],
            "principal": principal_1,
            "loss_given_default_pct": round(lgd_1, 4),
            "total_credit_loss": round(loss_1_total, 2),
            "bank_direct_loss": round(loss_1_bank, 2),
            "private_credit_loss": round(loss_1_shadow, 2),
        }

        # Channel 2: Bank Subscription Lines to Private Credit ($220B)
        # When private credit funds take hits from Channel 1 and illiquid venture assets,
        # subscription facilities face impairment.
        ch2 = self.channels["channel_2_bank_private_credit_leverage"]
        principal_2 = ch2["total_principal"]
        # Fund default probability scales with severity of Channel 1 losses
        fund_distress_factor = min(0.35, ai_contract_default_pct * 0.5)
        lgd_2 = 0.30  # recovery on fund assets / capital calls
        loss_2_bank = principal_2 * fund_distress_factor * lgd_2
        loss_2_shadow = 0.0  # absorbed by the lending banks

        channel_results["channel_2_bank_private_credit_leverage"] = {
            "name": ch2["name"],
            "principal": principal_2,
            "fund_distress_rate": round(fund_distress_factor, 4),
            "total_credit_loss": round(loss_2_bank, 2),
            "bank_direct_loss": round(loss_2_bank, 2),
            "private_credit_loss": 0.0,
        }

        # Channel 3: Bank Warehouse & Hung Bridge Loans ($55B)
        ch3 = self.channels["channel_3_bank_warehouse_bridge_loans"]
        principal_3 = ch3["total_principal"]
        loss_3_bank = principal_3 * warehouse_debt_markdown_pct
        loss_3_shadow = 0.0

        channel_results["channel_3_bank_warehouse_bridge_loans"] = {
            "name": ch3["name"],
            "principal": principal_3,
            "markdown_pct": warehouse_debt_markdown_pct,
            "total_credit_loss": round(loss_3_bank, 2),
            "bank_direct_loss": round(loss_3_bank, 2),
            "private_credit_loss": 0.0,
        }

        # Channel 4: Data Center CMBS & CRE ($145B)
        ch4 = self.channels["channel_4_datacenter_cre_cmbs"]
        principal_4 = ch4["total_principal"]
        lgd_4 = 0.38  # specialized real estate with stranded power PPAs
        loss_4_total = principal_4 * cre_datacenter_default_pct * lgd_4
        loss_4_bank = loss_4_total * ch4["bank_direct_exposure_share"]
        loss_4_shadow = loss_4_total * ch4["shadow_bank_private_credit_share"]

        channel_results["channel_4_datacenter_cre_cmbs"] = {
            "name": ch4["name"],
            "principal": principal_4,
            "default_rate": cre_datacenter_default_pct,
            "total_credit_loss": round(loss_4_total, 2),
            "bank_direct_loss": round(loss_4_bank, 2),
            "private_credit_loss": round(loss_4_shadow, 2),
        }

        # Channel 5: Utility & Grid Corporate Debt ($180B)
        # Duration ~6.5 years: Mark-to-market loss = Duration * delta_spread
        ch5 = self.channels["channel_5_utility_grid_capex_debt"]
        principal_5 = ch5["total_principal"]
        duration = 6.5
        bond_price_decline_pct = min(0.30, duration * (utility_spread_widening_bps / 10000.0))
        loss_5_total = principal_5 * bond_price_decline_pct
        loss_5_bank = loss_5_total * ch5["bank_direct_exposure_share"]
        loss_5_shadow = loss_5_total * ch5["shadow_bank_private_credit_share"]

        channel_results["channel_5_utility_grid_capex_debt"] = {
            "name": ch5["name"],
            "principal": principal_5,
            "spread_widening_bps": utility_spread_widening_bps,
            "bond_price_decline_pct": round(bond_price_decline_pct, 4),
            "total_credit_loss": round(loss_5_total, 2),
            "bank_direct_loss": round(loss_5_bank, 2),
            "private_credit_loss": round(loss_5_shadow, 2),
        }

        # Aggregate losses
        for res in channel_results.values():
            total_system_losses += res["total_credit_loss"]
            total_bank_losses += res["bank_direct_loss"]
            total_shadow_bank_losses += res["private_credit_loss"]

        # Bank Capital Stress Impact
        base_cet1 = self.bank_baseline["total_cet1_capital"]
        rwa = self.bank_baseline["total_risk_weighted_assets"]
        base_ratio = base_cet1 / rwa
        reg_min = self.bank_baseline["regulatory_minimum_cet1_threshold"]
        contraction_mult = self.bank_baseline["credit_contraction_multiplier"]

        stressed_cet1 = base_cet1 - total_bank_losses
        stressed_ratio = stressed_cet1 / rwa
        cet1_depletion_bps = (base_ratio - stressed_ratio) * 10000.0

        # Credit Contraction: Banks reduce general balance sheet lending to rebuild ratios
        macro_credit_contraction = total_bank_losses * contraction_mult

        capital_breached = stressed_ratio < reg_min

        return {
            "parameters": {
                "gpu_hardware_haircut_pct": gpu_hardware_haircut_pct,
                "ai_contract_default_pct": ai_contract_default_pct,
                "warehouse_debt_markdown_pct": warehouse_debt_markdown_pct,
                "cre_datacenter_default_pct": cre_datacenter_default_pct,
                "utility_spread_widening_bps": utility_spread_widening_bps,
            },
            "channel_losses": channel_results,
            "aggregate_losses": {
                "total_financial_system_losses": round(total_system_losses, 2),
                "commercial_bank_losses": round(total_bank_losses, 2),
                "shadow_bank_private_credit_losses": round(total_shadow_bank_losses, 2),
            },
            "commercial_bank_capital_impact": {
                "baseline_cet1_capital": base_cet1,
                "stressed_cet1_capital": round(stressed_cet1, 2),
                "baseline_cet1_ratio": round(base_ratio, 4),
                "stressed_cet1_ratio": round(stressed_ratio, 4),
                "cet1_depletion_bps": round(cet1_depletion_bps, 1),
                "regulatory_minimum_threshold": reg_min,
                "regulatory_buffer_breached": capital_breached,
                "implied_macro_credit_contraction": round(macro_credit_contraction, 2),
            },
        }

    def run_predefined_stress_levels(self) -> Dict[str, Any]:
        """
        Runs three canonical banking stress levels:
        1. mild_repricing: Minor GPU resale decline, modest contract renegotiations.
        2. base_bubble_burst: 60% GPU haircut, 45% contract default, warehouse hung debt.
        3. systemic_credit_crunch: 80% GPU collapse, 70% contract defaults, widespread private debt distress.
        """
        stress_levels = {
            "mild_repricing": {
                "gpu_hardware_haircut_pct": 0.35,
                "ai_contract_default_pct": 0.20,
                "warehouse_debt_markdown_pct": 0.12,
                "cre_datacenter_default_pct": 0.05,
                "utility_spread_widening_bps": 100.0,
            },
            "base_bubble_burst": {
                "gpu_hardware_haircut_pct": 0.60,
                "ai_contract_default_pct": 0.45,
                "warehouse_debt_markdown_pct": 0.25,
                "cre_datacenter_default_pct": 0.12,
                "utility_spread_widening_bps": 200.0,
            },
            "systemic_credit_crunch": {
                "gpu_hardware_haircut_pct": 0.80,
                "ai_contract_default_pct": 0.70,
                "warehouse_debt_markdown_pct": 0.40,
                "cre_datacenter_default_pct": 0.22,
                "utility_spread_widening_bps": 350.0,
            },
        }

        return {k: self.simulate_stress_scenario(**v) for k, v in stress_levels.items()}


if __name__ == "__main__":
    model = BankingContagionModel()
    results = model.run_predefined_stress_levels()
    for name, res in results.items():
        agg = res["aggregate_losses"]
        cap = res["commercial_bank_capital_impact"]
        print(f"\n=== Stress Level: {name} ===")
        print(f"Total System Losses: ${agg['total_financial_system_losses']:,.0f}")
        print(f"Commercial Bank Losses: ${agg['commercial_bank_losses']:,.0f}")
        print(f"Private Credit Losses: ${agg['shadow_bank_private_credit_losses']:,.0f}")
        print(f"Stressed CET1 Ratio: {cap['stressed_cet1_ratio']:.2%} (from {cap['baseline_cet1_ratio']:.2%})")
        print(f"Capital Depleted: {cap['cet1_depletion_bps']:.0f} bps")
        print(f"Implied Macro Credit Contraction: ${cap['implied_macro_credit_contraction']:,.0f}")
