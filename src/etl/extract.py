import pandas as pd
import os
from logger import get_logger

logger = get_logger()

def extract_data(folder_path: str, dataset_id: str = "FD001"):
    """
    Extract train, test, and RUL data for a specific NASA CMAPSS dataset (e.g. FD001).
    """
    try:
        logger.info(f"Starting extraction for dataset {dataset_id} in folder: {folder_path}")

        # Build file paths
        train_path = os.path.join(folder_path, f"train_{dataset_id}.txt")
        test_path = os.path.join(folder_path, f"test_{dataset_id}.txt")
        rul_path = os.path.join(folder_path, f"RUL_{dataset_id}.txt")

        # Read files
        train_df = pd.read_csv(train_path, sep=r'\s+', header=None).dropna(axis=1, how='all')
        test_df = pd.read_csv(test_path, sep=r'\s+', header=None).dropna(axis=1, how='all')
        rul_df = pd.read_csv(rul_path, sep=r'\s+', header=None)

        logger.info(f"✅ Extracted: train({len(train_df)} rows), test({len(test_df)} rows), RUL({len(rul_df)} rows)")
        return train_df, test_df, rul_df

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except Exception as e:
        logger.error(f"Error during extraction: {e}")
        raise

