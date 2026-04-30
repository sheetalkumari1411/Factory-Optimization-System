from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import encode_features
from src.model_training import train_models
from src.evaluation import evaluate

df = load_data("data/raw/data.csv")
df = preprocess_data(df)
df, encoders = encode_features(df)

models, X_test, y_test = train_models(df)

for name, model in models.items():
    metrics = evaluate(model, X_test, y_test)
    print(name, metrics)