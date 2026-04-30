def optimize(simulation_results):
    # Sort by lowest lead time
    ranked = sorted(simulation_results, key=lambda x: x['predicted_lead_time'])

    best = ranked[0]

    return best, ranked