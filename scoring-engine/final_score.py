def calculate_final_score(freshness, volume, schema, impact):
    """
    Weighted final trust score.
    """

    weights = {
        "freshness": 0.35,
        "volume": 0.25,
        "schema": 0.20,
        "impact": 0.20
    }

    final_score = (
        freshness * weights["freshness"] +
        volume * weights["volume"] +
        schema * weights["schema"] +
        impact * weights["impact"]
    )

    return round(final_score, 2)
