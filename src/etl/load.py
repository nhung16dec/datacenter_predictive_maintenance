import psycopg2
from psycopg2.extras import execute_values
from logger import get_logger

logger = get_logger()

def load_data(df, conn_params, table_name="sensor_data"):
    """
    Charge un DataFrame dans PostgreSQL.
    df: DataFrame pandas à charger
    conn_params: dictionnaire de connexion
    table_name: nom de la table cible
    """
    try:
        logger.info(f"Connecting to PostgreSQL for table {table_name}")
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()

        # Crée la table si elle n'existe pas, on adapte les colonnes dynamiquement
        columns = df.columns
        columns_def = ",\n".join([f"{col} TEXT" for col in columns])
        create_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {columns_def}
        )
        """
        cur.execute(create_query)
        logger.info(f"Table {table_name} ensured in database")

        # Insertion rapide avec execute_values
        values = [tuple(row) for row in df.values]
        cols = ",".join(columns)
        insert_query = f"INSERT INTO {table_name} ({cols}) VALUES %s"
        execute_values(cur, insert_query, values)

        conn.commit()
        cur.close()
        conn.close()
        logger.info(f"Loaded successfully {len(df)} rows into {table_name}")

    except psycopg2.OperationalError as e:
        logger.error(f"Database connection error: {e}")
        raise
    except Exception as e:
        logger.error(f"Error during loading: {e}")
        raise

