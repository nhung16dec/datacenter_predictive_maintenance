from logger import get_logger

logger = get_logger()

def transform_data(df):
    try:
        logger.info("Starting transformaton")
        df["temperature_C"] = df["temperature"]
        df["temperature_F"] = df["temperature"] * 9/5 + 32
        logger.info("Transform: Added Fahrenheit column")
        return df
    except KeyError as e:
        logger.info("Missing column in data: {e}")
        raise
    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        raise

