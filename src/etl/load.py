import psycopg2
from psycopg2.extras import execute_values
from logger import get_logger
logger = get_logger()

def load_data(df, conn_params):
    try:
        logger.info("Connecting to PostgreSQL")
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS sensor_data (
                sensor_id INT,
                temperature FLOAT,
                humidity FLOAT,
                timestamp TIMESTAMP,
                temperature_F FLOAT
            )
        """)
        logger.info("Table ensured in database")

        values = [tuple(row) for row in df[["sensor_id", "temperature", "humidity", "timestamp", "temperature_F"]].values]
        execute_values(cur, "INSERT INTO sensor_data VALUES %s", values)

        conn.commit()
        cur.close()
        conn.close()
        logger.info(f"Loaded sucessfuly {len(df)} rows into database")

    except psycopg2.OperationalError as e:
        logger.error(f"Database connection error: {e}")
        raise
    except Exception as e:
        logger.error(f"Error during loading: {e}")
        raise

