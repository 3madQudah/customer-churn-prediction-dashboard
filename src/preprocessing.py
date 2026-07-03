import pandas as pd


def preprocess_input(data, encoders, scaler):
    """
    data : dict
    encoders : dictionary of LabelEncoders
    scaler : StandardScaler
    """

    df = pd.DataFrame([data])

    # Convert TotalCharges
    df["TotalCharges"] = df["TotalCharges"].astype(float)

    # Encode categorical columns
    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = encoder.transform(df[col])

    # Scale all features
    df_scaled = scaler.transform(df)

    return df_scaled