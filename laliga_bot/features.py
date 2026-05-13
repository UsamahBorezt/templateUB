import pandas as pd

from laliga_bot.config import ROLLING_WINDOW


def _result_points(goals_for: int, goals_against: int) -> int:
    if goals_for > goals_against:
        return 3
    if goals_for == goals_against:
        return 1
    return 0


def add_team_form_features(matches: pd.DataFrame) -> pd.DataFrame:
    records = []
    team_history = {}

    for _, row in matches.iterrows():
        home = row["home_team"]
        away = row["away_team"]

        home_hist = team_history.get(home, [])
        away_hist = team_history.get(away, [])

        rec = row.to_dict()
        rec["home_form_points_avg"] = (
            sum(home_hist[-ROLLING_WINDOW:]) / min(len(home_hist), ROLLING_WINDOW)
            if home_hist
            else 0.0
        )
        rec["away_form_points_avg"] = (
            sum(away_hist[-ROLLING_WINDOW:]) / min(len(away_hist), ROLLING_WINDOW)
            if away_hist
            else 0.0
        )
        rec["form_diff"] = rec["home_form_points_avg"] - rec["away_form_points_avg"]

        records.append(rec)

        home_pts = _result_points(int(row["home_goals"]), int(row["away_goals"]))
        away_pts = _result_points(int(row["away_goals"]), int(row["home_goals"]))
        team_history.setdefault(home, []).append(home_pts)
        team_history.setdefault(away, []).append(away_pts)

    return pd.DataFrame(records)


def add_target_label(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["target"] = out.apply(
        lambda r: "H" if r["home_goals"] > r["away_goals"] else ("D" if r["home_goals"] == r["away_goals"] else "A"),
        axis=1,
    )
    return out
