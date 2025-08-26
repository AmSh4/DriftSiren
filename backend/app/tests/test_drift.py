from app.ml.drift import compute_psi, compute_ks, compute_chi2

def test_metrics_basic():
    base = [{"x": i} for i in range(100)]
    curr = [{"x": i+5} for i in range(100)]
    assert compute_psi(base, curr) >= 0.0
    assert compute_ks(base, curr) >= 0.0
    assert compute_chi2(base, curr) >= 0.0
