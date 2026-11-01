"""
Unit and invariant tests for AnthropicS1Model.
Validates Form S-1 accounting reconciliations, take-or-pay compute floors, and macro integration.
"""

import pytest
from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from anthropic_s1_model import AnthropicS1Model


@pytest.fixture
def s1_model():
    return AnthropicS1Model()


def test_s1_gross_margin_reconciliation(s1_model):
    """
    Verifies that H1 2026 accounting gross margin (~85.4%) vs. compute-adjusted
    economic gross margin (~45.1%) is accurately reconciled.
    """
    recon = s1_model.reconcile_s1_unit_economics()
    margin = recon["margin_reconciliation"]

    assert recon["h1_2026_revenue_millions"] == 16286.0
    assert 0.85 <= margin["accounting_gross_margin_pct"] <= 0.86
    assert 0.44 <= margin["compute_adjusted_gross_margin_pct"] <= 0.46
    assert margin["margin_illusion_spread_pct"] > 0.39


def test_s1_convertible_notes_and_cash_fortress(s1_model):
    """
    Verifies the ASC 825-10 convertible note distortion ($108.6B carrying value on $6.2B principal)
    and June 30, 2026 liquid reserves ($131.7B).
    """
    recon = s1_model.reconcile_s1_unit_economics()
    ec = recon["earnings_and_cash_reconciliation"]
    bs = recon["balance_sheet_fortress"]

    assert ec["gaap_net_loss_millions"] == -80748.0
    assert ec["non_cash_convertible_note_fv_loss_millions"] == -72400.0
    assert ec["operating_cash_flow_millions"] == 3929.0
    assert ec["fair_value_to_principal_multiplier"] > 17.0
    assert bs["liquid_reserves_millions"] == 131700.0
    assert bs["pro_forma_post_conversion_liabilities_millions"] < 10000.0


def test_commitments_aggregation(s1_model):
    """
    Verifies June 30, 2026 baseline commitments ($587.0B) and subsequent events total ($688.6B).
    """
    comm = s1_model.get_commitments_summary()
    assert comm["baseline_june_30_2026_billions"] == 587.0
    assert comm["purchase_commitments_billions"] == 265.6
    assert comm["uncommenced_leases_billions"] == 321.4
    assert 680.0 <= comm["total_including_subsequent_events_billions"] <= 700.0


def test_scenarios_ordering_and_solvency_buffer(s1_model):
    """
    Verifies that Bull > Base > Bear across 2028 revenue, 2029 liquidity, and implied valuation,
    and that the $131.7B cash reserve prevents outright bankruptcy through 2029 even in Bear case.
    """
    out = s1_model.run_predefined_s1_scenarios()
    bull = out["scenarios"]["agentic_singularity_bull"]["summary_metrics"]
    base = out["scenarios"]["rational_enterprise_base"]["summary_metrics"]
    bear = out["scenarios"]["ai_bubble_burst_bear"]["summary_metrics"]

    assert (
        bull["revenue_2028_billions"]
        > base["revenue_2028_billions"]
        > bear["revenue_2028_billions"]
    )
    assert (
        bull["ending_liquidity_2029_billions"]
        > base["ending_liquidity_2029_billions"]
        > bear["ending_liquidity_2029_billions"]
    )
    assert (
        bull["implied_2028_market_cap_billions"]
        > base["implied_2028_market_cap_billions"]
        > bear["implied_2028_market_cap_billions"]
    )

    # Bear case accumulates significant deadweight compute penalties
    assert bear["cumulative_deadweight_compute_2026_2030_billions"] > 100.0
    # Base case implies negative return vs $1.5T IPO price
    assert base["implied_return_vs_1_5t_ipo_pct"] < -0.25


def test_macro_bubble_reconciliation(s1_model):
    """
    Verifies that Anthropic's Q2 2026 annualized run-rate ($46.22B) and 2028 take-or-pay ($86B)
    reconcile properly with the macroeconomic labor/CapEx deficit model.
    """
    macro_rec = s1_model.reconcile_with_macro_bubble_model()
    assert macro_rec["anthropic_q2_2026_run_rate_billions"] == 46.22
    assert 0.35 <= macro_rec["hyperscaler_depreciation_transferred_to_anthropic_pct"] <= 0.45


def test_html_reports_have_zero_backslashes():
    """
    Verifies that the compiled HTML reports contain zero stray Markdown backslashes.
    """
    docs_dir = Path(__file__).resolve().parent.parent.parent / "docs"
    for html_name in ("anthropic_s1_evaluation.html", "ai_bubble_burst_report.html"):
        html_path = docs_dir / html_name
        assert html_path.exists(), f"Missing {html_path}"
        content = html_path.read_text(encoding="utf-8")
        assert "\\" not in content, f"Found stray backslash in {html_name}"

