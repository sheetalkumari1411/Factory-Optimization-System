from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression


def train_models(df):

    # -----------------------------
    # Drop non-numeric / useless columns
    # -----------------------------
    drop_cols = [
        'Row ID',
        'Order ID',
        'Customer ID',
        'Product ID',
        'Product Name',
        'City',
        'State/Province',
        'Country/Region',
        'Order Date',
        'Ship Date'
    ]

    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

    # -----------------------------
    # Convert categorical columns
    # -----------------------------
    df = df.copy()

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category').cat.codes

    # -----------------------------
    # Split features and target
    # -----------------------------
    X = df.drop(columns=['Lead Time'])
    y = df['Lead Time']

    # -----------------------------
    # Train-test split
    # -----------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -----------------------------
    # Models
    # -----------------------------
    models = {
        "linear": LinearRegression(),
        "random_forest": RandomForestRegressor(),
        "gradient_boosting": GradientBoostingRegressor()
    }

    trained_models = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model

    return trained_models, X_test, y_test