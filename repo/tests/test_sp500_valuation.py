"""
Unit and boundary tests for SP500ValuationModel.
Validates cohort weights, drawdown calculations, and scenario consistency.
"""

import pytest
from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from sp500_valuation_model import SP500ValuationModel


@pytest.fixture
def model():
    return SP500ValuationModel()


def test_cohort_weights_sum_to_one(model):
    """Verifies that all 4 cohort index weights sum to exactly 1.0 (100%)."""
    total_weight = sum(c["index_weight"] for c in model.cohorts)
    assert abs(total_weight - 1.0) < 0.0001
    assert len(model.cohorts) == 4


def test_zero_shock_invariance(model):
    """Zero capex cut and zero multiple de-rating must yield zero drawdown."""
    res = model.simulate_crash(
        capex_cut_pct=0.0,
        multiple_derate_severity=0.0,
        macro_wealth_drag_pct=0.0,
        bank_credit_drag_pct=0.0,
    )
    summary = res["index_summary"]
    assert abs(summary["peak_to_trough_drawdown_pct"]) < 0.0001
    assert abs(summary["stressed_index_level"] - summary["base_index_level"]) < 0.1
    assert abs(summary["stressed_aggregate_eps"] - summary["base_aggregate_eps"]) < 0.1


def test_monotonicity_of_scenarios(model):
    """Drawdown must strictly worsen as scenario severity increases."""
    scenarios = model.run_predefined_crash_scenarios()
    mild = scenarios["mild_disillusionment"]["index_summary"]["peak_to_trough_drawdown_pct"]
    base = scenarios["base_bubble_burst"]["index_summary"]["peak_to_trough_drawdown_pct"]
    systemic = scenarios["systemic_liquidity_bust"]["index_summary"]["peak_to_trough_drawdown_pct"]

    # Drawdowns are negative numbers (e.g. -0.23 > -0.40 > -0.52)
    assert mild > base > systemic
    assert -0.25 <= mild <= -0.20
    assert -0.45 <= base <= -0.35
    assert -0.55 <= systemic <= -0.45


def test_silicon_bullwhip_dominance(model):
    """Silicon enablers must suffer the highest percentage price drop in the base crash."""
    res = model.simulate_crash()
    cohorts = {c["id"]: c["price_change_pct"] for c in res["cohort_breakdown"]}
    assert cohorts["cohort_1_silicon_enablers"] < cohorts["cohort_2_hyperscalers"]
    assert cohorts["cohort_1_silicon_enablers"] < cohorts["cohort_4_broader_market"]
