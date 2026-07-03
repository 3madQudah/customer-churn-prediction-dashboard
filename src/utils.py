import joblib
from pathlib import Path

# Root project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Models directory
MODELS_DIR = BASE_DIR / "models"

MODEL_PATH = MODELS_DIR / "best_model.pkl"
SCALER_PATH = MODELS_DIR / "scaler.pkl"
ENCODER_PATH = MODELS_DIR / "label_encoders.pkl"
TARGET_ENCODER_PATH = MODELS_DIR / "target_encoder.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def load_scaler():
    return joblib.load(SCALER_PATH)


def load_encoders():
    return joblib.load(ENCODER_PATH)


def load_target_encoder():
    return joblib.load(TARGET_ENCODER_PATH)