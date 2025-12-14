def calculate_volume_score(current_row_count, historical_avg_row_count):
    """
    Detects unusual drops or spikes in row volume.
    """

    if historical_avg_row_count == 0:
        return 100

    deviation = abs(current_row_count - historical_avg_row_count) / historical_avg_row_count

    if deviation <= 0.1:
        return 100
    elif deviation <= 0.25:
        return 75
    elif deviation <= 0.5:
        return 40
    else:
        return 10
