import pandas as pd

REQUIRED_COLUMNS = {"date", "home_team", "away_team", "home_goals", "away_goals"}


def load_matches(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Kolom wajib tidak lengkap: {sorted(missing)}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if df["date"].isna().any():
        raise ValueError("Ada nilai date yang tidak valid.")

    df = df.sort_values("date").reset_index(drop=True)
    return df
