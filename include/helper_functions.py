import pandas as pd
import numpy as np

def canonical_line(x):
    if pd.isna(x):
        return "UNKNOWN"

    s = str(x).upper().replace(" ", "")

    present = set()
    if "YU" in s:
        present.add("YU")
    if "BD" in s:
        present.add("BD")
    if "SHP" in s:
        present.add("SHP")
    if "SRT" in s:
        present.add("SRT")

    order = ["YU", "BD", "SHP", "SRT"]
    tokens = [t for t in order if t in present]

    return "/".join(tokens) if tokens else "UNKNOWN"

def canonical_bound(x):
    if pd.isna(x):
        return pd.NA

    s = str(x).strip().upper()

    mapping = {
        "N": "N", "NB": "N", "NORTH": "N",
        "S": "S", "SB": "S", "SOUTH": "S",
        "E": "E", "EB": "E", "EAST": "E",
        "W": "W", "WB": "W", "WEST": "W",
    }
    return mapping.get(s, pd.NA)


Z_THRESH = 6
def mad_outlier_mask(series: pd.Series, z_thresh: float = Z_THRESH) -> pd.Series:
    x = series.to_numpy(dtype=float)
    med = np.median(x)
    mad = np.median(np.abs(x - med))

    if mad == 0 or np.isnan(mad):
        return pd.Series(False, index=series.index)

    robust_z = 0.6745 * (x - med) / mad
    return pd.Series(np.abs(robust_z) > z_thresh, index=series.index)
