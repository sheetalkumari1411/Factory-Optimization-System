import pandas as pd

def load_data(path):
    """
    Load dataset from CSV file
    """
    df = pd.read_csv(path)
    return df


def preprocess_data(df):
    """
    Clean and prepare dataset
    """

    df = df.copy()

    # -----------------------------
    # Convert date columns properly
    # -----------------------------
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

    # -----------------------------
    # Create Lead Time
    # -----------------------------
    df['Lead Time'] = (df['Ship Date'] - df['Order Date']).dt.days

    # -----------------------------
    # Remove invalid or negative lead times
    # -----------------------------
    df = df[df['Lead Time'] >= 0]

    # -----------------------------
    # Drop missing values
    # -----------------------------
    df = df.dropna()

    # -----------------------------
    # Remove extreme outliers (optional but good)
    # -----------------------------
    df = df[df['Lead Time'] < df['Lead Time'].quantile(0.99)]

    return df