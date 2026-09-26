"""
Unit and boundary tests for BankingContagionModel.
Validates multi-channel debt transmission, bank capital ratios, and credit contraction formulas.
"""

import pytest
from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from banking_contagion_model import BankingContagionModel


@pytest.fixture
def model():
    return BankingContagionModel()


def test_baseline_capital_consistency(model):
    """Verifies baseline CET1 capital and ratio math."""
    base = model.bank_baseline
    calculated_ratio = base["total_cet1_capital"] / base["total_risk_weighted_assets"]
    assert abs(calculated_ratio - base["baseline_cet1_ratio"]) < 0.0001


def test_zero_stress_scenario(model):
    """When all stress parameters are zero, losses must be zero and CET1 unchanged."""
    res = model.simulate_stress_scenario(
        gpu_hardware_haircut_pct=0.0,
        ai_contract_default_pct=0.0,
        warehouse_debt_markdown_pct=0.0,
        cre_datacenter_default_pct=0.0,
        utility_spread_widening_bps=0.0,
    )
    agg = res["aggregate_losses"]
    cap = res["commercial_bank_capital_impact"]
    assert agg["total_financial_system_losses"] == 0.0
    assert agg["commercial_bank_losses"] == 0.0
    assert cap["cet1_depletion_bps"] == 0.0
    assert cap["stressed_cet1_ratio"] == cap["baseline_cet1_ratio"]


def test_monotonicity_of_stress_severity(model):
    """Higher stress levels must strictly increase losses and bank capital depletion."""
    stress_outputs = model.run_predefined_stress_levels()
    mild = stress_outputs["mild_repricing"]
    base = stress_outputs["base_bubble_burst"]
    severe = stress_outputs["systemic_credit_crunch"]

    assert mild["aggregate_losses"]["total_financial_system_losses"] < base["aggregate_losses"]["total_financial_system_losses"]
    assert base["aggregate_losses"]["total_financial_system_losses"] < severe["aggregate_losses"]["total_financial_system_losses"]

    assert mild["commercial_bank_capital_impact"]["cet1_depletion_bps"] < base["commercial_bank_capital_impact"]["cet1_depletion_bps"]
    assert base["commercial_bank_capital_impact"]["cet1_depletion_bps"] < severe["commercial_bank_capital_impact"]["cet1_depletion_bps"]


def test_channel_loss_partition(model):
    """Verifies bank losses + private credit losses equal total losses across channels."""
    res = model.simulate_stress_scenario()
    agg = res["aggregate_losses"]
    sum_parts = agg["commercial_bank_losses"] + agg["shadow_bank_private_credit_losses"]
    assert abs(sum_parts - agg["total_financial_system_losses"]) < 1.0  # within rounding
