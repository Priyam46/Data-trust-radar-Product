from datetime import datetime, timedelta

def calculate_freshness_score(last_updated_timestamp, expected_frequency_hours):
    """
    Scores how fresh the dataset is compared to expected refresh frequency.
    """

    now = datetime.utcnow()
    delay_hours = (now - last_updated_timestamp).total_seconds() / 3600

    if delay_hours <= expected_frequency_hours:
        return 100
    elif delay_hours <= expected_frequency_hours * 1.5:
        return 70
    elif delay_hours <= expected_frequency_hours * 2:
        return 40
    else:
        return 10
