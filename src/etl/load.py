import psycopg2
from psycopg2.extras import execute_values

def load_data(df, conn_params):
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

    values = [tuple(row) for row in df[["sensor_id", "temperature", "humidity", "timestamp", "temperature_F"]].values]
    execute_values(cur, "INSERT INTO sensor_data VALUES %s", values)

    conn.commit()
    cur.close()
    conn.close()
    print(f"Loaded {len(df)} rows into database")

