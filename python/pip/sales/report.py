"""Sales aggregation using the pandas 1.x API.

Both idioms used here are removed in pandas 2.0:
- `DataFrame.append()` was removed in 2.0 (use `pd.concat`).
- `DataFrame.iteritems()` was removed in 2.0 (use `.items()`).
"""
import pandas as pd


def build_frame(rows: list[dict]) -> pd.DataFrame:
    # Start empty and grow with append() — the classic 1.x pattern.
    # (No predefined columns so numeric dtypes are inferred from the data.)
    df = pd.DataFrame()
    for row in rows:
        df = df.append(row, ignore_index=True)
    return df


def column_totals(df: pd.DataFrame) -> dict:
    totals = {}
    # 1.x: iteritems(). Removed in 2.0 -> .items().
    for name, series in df.iteritems():
        if pd.api.types.is_numeric_dtype(series):
            totals[name] = series.sum()
    return totals


def revenue(df: pd.DataFrame) -> float:
    return float((df["qty"] * df["price"]).sum())
