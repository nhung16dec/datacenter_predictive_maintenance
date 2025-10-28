import os
from dotenv import load_dotenv
from extract import extract_data
from transform import transform_data
from load import load_data
from logger import get_logger

logger = get_logger()
load_dotenv()  # charge les variables d'environnement depuis .env

conn_params = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT")
}

if __name__ == "__main__":
    # ---------------------------------------
    # 1️⃣ Extraction des fichiers NASA
    # ---------------------------------------
    folder_path = "../../data"  # dossier contenant FD001..FD004
    extracted_dfs = extract_data(folder_path)  # retourne [train_df, test_df, rul_df]
    train_df, test_df, rul_df = extracted_dfs

    logger.info(f"Train shape: {train_df.shape}, Test shape: {test_df.shape}, RUL shape: {rul_df.shape}")

    # ---------------------------------------
    # 2️⃣ Transformation
    # ---------------------------------------
    train_df = transform_data(train_df, data_type="train")
    test_df = transform_data(test_df, data_type="test")
    # On peut ajouter RUL au test_df si nécessaire
    test_df["RUL"] = rul_df

    logger.info("Transformation done")

    # ---------------------------------------
    # 3️⃣ Chargement dans PostgreSQL
    # ---------------------------------------
    load_data(train_df, conn_params, table_name="nasa_train")
    load_data(test_df, conn_params, table_name="nasa_test")

    logger.info("ETL pipeline completed successfully")

