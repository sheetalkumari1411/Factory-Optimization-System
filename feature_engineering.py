import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_features(df):
    df = df.copy()

    categorical_cols = ['Ship Mode', 'Region', 'Product Name']

    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    return df, encoders