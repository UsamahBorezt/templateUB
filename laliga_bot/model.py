from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from laliga_bot.config import MODEL_PATH, RANDOM_STATE

FEATURES = [
    "home_team",
    "away_team",
    "home_form_points_avg",
    "away_form_points_avg",
    "form_diff",
]


def build_pipeline() -> Pipeline:
    categorical = ["home_team", "away_team"]
    numeric = ["home_form_points_avg", "away_form_points_avg", "form_diff"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
            ("num", StandardScaler(), numeric),
        ]
    )

    clf = LogisticRegression(max_iter=2000, random_state=RANDOM_STATE, multi_class="multinomial")

    return Pipeline([("preprocess", preprocessor), ("clf", clf)])


def train_model(df_train: pd.DataFrame) -> Pipeline:
    X = df_train[FEATURES]
    y = df_train["target"]

    pipe = build_pipeline()
    pipe.fit(X, y)

    Path(MODEL_PATH).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, MODEL_PATH)
    return pipe


def load_model() -> Pipeline:
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model belum ada. Jalankan mode train terlebih dahulu.")
    return joblib.load(MODEL_PATH)


def predict_proba(pipe: Pipeline, df: pd.DataFrame) -> pd.DataFrame:
    X = df[FEATURES]
    probas = pipe.predict_proba(X)
    classes = list(pipe.classes_)

    out = df[["date", "home_team", "away_team"]].copy()
    for idx, cls in enumerate(classes):
        out[f"p_{cls}"] = probas[:, idx]
    out["pred"] = pipe.predict(X)
    return out
