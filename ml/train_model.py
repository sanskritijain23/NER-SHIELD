"""
ml/train_model.py
------------------
Owner: Member 2 (ML)

Responsibility:
    Train a Scikit-learn model on the processed landslide dataset and
    save the trained model to disk for later use by ml/predict.py.

Input:
    data/processed/landslide_data.csv

Output:
    models/landslide_model.pkl

NOTE: This is a placeholder. No real training logic, no fake/mocked
data, and no dummy model is implemented yet. Everything below is a
scaffold marking what needs to be built.
"""

import os

# TODO (Member 2): import what you actually need once implementing, e.g.
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier  # or any chosen model
# import joblib

PROCESSED_DATA_PATH = os.path.join("data", "processed", "landslide_data.csv")
MODEL_OUTPUT_PATH = os.path.join("models", "landslide_model.pkl")


def load_processed_data(csv_path: str = PROCESSED_DATA_PATH):
    """
    Load the processed landslide dataset for training.

    Args:
        csv_path: Path to the processed CSV file produced by Member 1.

    Returns:
        A pandas DataFrame with the training data.

    TODO (Member 2): Implement using pandas.read_csv once
    data/processed/landslide_data.csv is available from Member 1.
    """
    raise NotImplementedError(
        "TODO: load and return the processed dataset from CSV."
    )


def train_model(data):
    """
    Train a Scikit-learn model on the given dataset.

    Args:
        data: A pandas DataFrame containing features + target
              (e.g. rainfall, slope, elevation, previous_landslide -> risk).

    Returns:
        A trained Scikit-learn model/estimator.

    TODO (Member 2):
        - Select features and target column(s).
        - Split into train/test sets.
        - Choose and train an appropriate model
          (e.g. RandomForestClassifier / RandomForestRegressor).
        - Evaluate the model (accuracy, F1, RMSE, etc. as appropriate).
    """
    raise NotImplementedError("TODO: implement model training logic.")


def save_model(model, output_path: str = MODEL_OUTPUT_PATH):
    """
    Persist the trained model to disk so ml/predict.py can load it.

    Args:
        model: The trained Scikit-learn model.
        output_path: Where to save the model (default: models/landslide_model.pkl).

    TODO (Member 2): Implement using joblib.dump(model, output_path).
    Make sure the `models/` directory exists before saving.
    """
    raise NotImplementedError("TODO: implement model saving with joblib.")


def main():
    """
    Orchestrates the training pipeline:
        1. Load processed data.
        2. Train the model.
        3. Save the trained model to models/landslide_model.pkl.

    TODO (Member 2): Wire the functions above together once implemented.
    """
    # PLACEHOLDER — do not run until the functions above are implemented.
    print("ml/train_model.py: training pipeline not implemented yet.")


if __name__ == "__main__":
    main()
