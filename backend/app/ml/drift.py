import numpy as np
from scipy.stats import ks_2samp, chisquare
from .utils import to_numeric_columns

def compute_psi(baseline_records, current_records, bins=10):
    psi_total = 0.0
    cols = to_numeric_columns(baseline_records | current_records if isinstance(baseline_records, dict) else {})
    # If dict trick fails, fall back:
    cols = to_numeric_columns(baseline_records + current_records)
    for name, _ in cols.items():
        base = np.array([r.get(name, np.nan) for r in baseline_records], dtype=float)
        curr = np.array([r.get(name, np.nan) for r in current_records], dtype=float)
        base = base[np.isfinite(base)]
        curr = curr[np.isfinite(curr)]
        if base.size < 2 or curr.size < 2:
            continue
        qs = np.quantile(base, np.linspace(0,1,bins+1))
        qs[0] = -np.inf; qs[-1] = np.inf
        b_hist, _ = np.histogram(base, bins=qs)
        c_hist, _ = np.histogram(curr, bins=qs)
        b_prop = np.clip(b_hist / max(b_hist.sum(), 1), 1e-6, 1)
        c_prop = np.clip(c_hist / max(c_hist.sum(), 1), 1e-6, 1)
        psi = np.sum((c_prop - b_prop) * np.log(c_prop / b_prop))
        psi_total += float(abs(psi))
    return float(psi_total)

def compute_ks(baseline_records, current_records):
    total = 0.0; n=0
    keys = set()
    for r in baseline_records + current_records:
        for k,v in r.items():
            if isinstance(v,(int,float)) and not isinstance(v,bool):
                keys.add(k)
    for k in keys:
        b = np.array([r.get(k, np.nan) for r in baseline_records], dtype=float)
        c = np.array([r.get(k, np.nan) for r in current_records], dtype=float)
        b = b[np.isfinite(b)]; c = c[np.isfinite(c)]
        if b.size<2 or c.size<2: 
            continue
        n+=1
        total += ks_2samp(b, c).statistic
    return float(total / n) if n else 0.0

def compute_chi2(baseline_records, current_records):
    # For numeric columns, bucketize into 10 bins and run chi2
    total = 0.0; n=0
    keys = set()
    for r in baseline_records + current_records:
        for k,v in r.items():
            if isinstance(v,(int,float)) and not isinstance(v,bool):
                keys.add(k)
    for k in keys:
        b = np.array([r.get(k, np.nan) for r in baseline_records], dtype=float)
        c = np.array([r.get(k, np.nan) for r in current_records], dtype=float)
        b = b[np.isfinite(b)]; c = c[np.isfinite(c)]
        if b.size<2 or c.size<2: 
            continue
        qs = np.quantile(b, np.linspace(0,1,11))
        qs[0] = -np.inf; qs[-1] = np.inf
        b_hist,_ = np.histogram(b, bins=qs)
        c_hist,_ = np.histogram(c, bins=qs)
        exp = b_hist + 1e-6
        obs = c_hist + 1e-6
        stat = chisquare(f_obs=obs, f_exp=exp).statistic
        total += float(stat)
        n+=1
    return float(total / n) if n else 0.0
