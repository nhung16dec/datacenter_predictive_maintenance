import pandas as pd

def extract_data(filepath: str):
    df = pd.read_csv(filepath)
    print(f"✅ Extracted {len(df)} rows from {filepath}")
    return df

