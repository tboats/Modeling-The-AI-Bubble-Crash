"""
Unit and invariant tests for LaborCapexModel.
Validates demographic math, wage savings calculations, and ROIC deficit boundaries.
"""

import pytest
from pathlib import Path
import sys

# Ensure repo/src is importable
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from labor_capex_model import LaborCapexModel


@pytest.fixture
def model():
    return LaborCapexModel()


def test_bls_headcount_sanity(model):
    """Verifies that total benchmark headcount sums to ~18 million knowledge workers."""
    res = model.compute_labor_savings()
    assert 17_500_000 <= res["total_benchmark_headcount"] <= 18_500_000
    assert len(res["occupations"]) == 7


def test_zero_displacement(model):
    """When displacement rates are 0%, wage savings must be zero."""
    zero_disp = {"global": {"junior": 0.0, "mid": 0.0, "senior": 0.0}}
    res = model.compute_labor_savings(custom_displacements=zero_disp)
    assert res["total_displaced_workers"] == 0
    assert res["total_gross_wage_savings"] == 0.0


def test_tech_and_law_savings_magnitude(model):
    """
    Verifies the user's specific scenario: ~20% displacement in software & law.
    Total wage savings should be between $90B and $130B.
    """
    scenarios = model.run_predefined_scenarios()
    tech_law = scenarios["tech_and_law_only"]
    assert 90_000_000_000 <= tech_law["gross_wage_savings"] <= 130_000_000_000
    assert tech_law["net_annual_deficit_big4"] < -100_000_000_000
    assert tech_law["roic_big4"] < -0.20


def test_subprime_comparison_assertion(model):
    """Confirms AI CapEx volume exceeds subprime mortgage peak issuance."""
    res = model.compute_capex_deficit()
    comp = res["subprime_mortgage_comparison"]
    assert comp["three_year_ai_capex"] > comp["subprime_peak_2004_2007"]
    assert comp["capex_to_subprime_ratio"] > 1.25


def test_monotonicity_of_displacement(model):
    """Higher displacement rates must strictly increase wage savings and reduce deficit."""
    low_disp = {"global": {"junior": 0.10, "mid": 0.05, "senior": 0.0}}
    high_disp = {"global": {"junior": 0.30, "mid": 0.15, "senior": 0.05}}

    res_low = model.compute_capex_deficit(custom_displacements=low_disp)
    res_high = model.compute_capex_deficit(custom_displacements=high_disp)

    assert res_high["gross_wage_savings"] > res_low["gross_wage_savings"]
    assert res_high["addressable_ai_software_revenue"] > res_low["addressable_ai_software_revenue"]
    assert res_high["roic_big4"] > res_low["roic_big4"]
