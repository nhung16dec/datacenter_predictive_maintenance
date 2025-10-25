import pandas as pd
from logger import get_logger

logger = get_logger()

def extract_data(filepath: str):
    try:
        df = pd.read_csv(filepath)
        logger.info(f"Starting extraction from {filepath}")
        print(f"✅ Extracted {len(df)} rows from {filepath}")
        logger.info(f"Extracted {len(df)}rows")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
    except Exception as e:
        logger.error(f"Error during extraction: {e}")
        raise
