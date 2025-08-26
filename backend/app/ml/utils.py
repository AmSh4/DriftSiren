import numpy as np

def to_numeric_columns(records):
    # flatten numeric values, ignore non-numeric
    keys = set()
    for r in records:
        for k,v in r.items():
            if isinstance(v, (int, float)) and not isinstance(v,bool):
                keys.add(k)
    arrs = {}
    for k in keys:
        arrs[k] = np.array([float(r.get(k, np.nan)) for r in records], dtype=float)
    return arrs
