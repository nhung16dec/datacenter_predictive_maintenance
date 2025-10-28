import pandas as pd
from logger import get_logger

logger = get_logger()

def transform_data(df: pd.DataFrame, data_type: str = None) -> pd.DataFrame:
    """
    Transforme les données du dataframe.
    - Ajoute éventuellement des colonnes spécifiques selon le type de données (train/test)
    """
    try:
        logger.info(f"Starting transformation for {data_type if data_type else 'dataset'}")
        df.columns = [
            "unit", "time", "op_setting1", "op_setting2", "op_setting3",
            "s1","s2","s3","s4","s5","s6","s7","s8","s9","s10",
            "s11","s12","s13","s14","s15","s16","s17","s18","s19","s20","s21"
        ]

        # Exemple : ajout d'une colonne de type Fahrenheit si température en Celsius
        if "temperature" in df.columns:
            df["temperature_F"] = df["temperature"] * 9/5 + 32

        # Ajout d'une colonne data_type pour différencier train/test
        if data_type:
            df["data_type"] = data_type


        logger.info(f"Transformation done for {data_type if data_type else 'dataset'}")
        return df

    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        raise

