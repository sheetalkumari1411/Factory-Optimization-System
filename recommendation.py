def generate_recommendation(current_factory, best_option):
    return {
        "current_factory": current_factory,
        "recommended_factory": best_option['factory'],
        "expected_lead_time": best_option['predicted_lead_time']
    }