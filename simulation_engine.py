from distance_calculator import FACTORIES

def simulate(product_row, model, feature_columns):
    results = []

    for factory in FACTORIES.keys():
        row = product_row.copy()
        row['Factory'] = factory

        X = row[feature_columns].values.reshape(1, -1)
        predicted_time = model.predict(X)[0]

        results.append({
            "factory": factory,
            "predicted_lead_time": predicted_time
        })

    return results