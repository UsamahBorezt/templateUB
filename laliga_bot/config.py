from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "output"
MODEL_PATH = MODEL_DIR / "wdl_model.joblib"

RANDOM_STATE = 42
ROLLING_WINDOW = 5
