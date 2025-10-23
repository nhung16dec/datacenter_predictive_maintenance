from extract import extract_data
from transform import transform_data
from load import load_data
from dotenv import load_dotenv
import os

load_dotenv()

conn_params = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT")
}


if __name__ == "__main__":   
    df = extract_data("../../data/sensors.csv")
    df = transform_data(df)
    load_data(df, conn_params)
