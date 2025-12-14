def calculate_impact_score(downstream_dashboards, business_criticality):
    """
    Higher impact datasets are penalized more strictly.
    """

    base_score = 100

    if downstream_dashboards > 5:
        base_score -= 20

    if business_criticality == "HIGH":
        base_score -= 30
    elif business_criticality == "MEDIUM":
        base_score -= 10

    return max(base_score, 10)
