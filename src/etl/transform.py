def transform_data(df):
    df["temperature_C"] = df["temperature"]
    df["temperature_F"] = df["temperature"] * 9/5 + 32
    print("Transform: Added Fahrenheit column")
    return df

