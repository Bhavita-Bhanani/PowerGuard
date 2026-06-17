def generate_insights(
    battery,
    cpu,
    ram,
    charging
):

    insights = []

    if battery < 30:
        insights.append(
            "Battery level is low."
        )

    if cpu > 80:
        insights.append(
            "High CPU usage detected."
        )

    if ram > 80:
        insights.append(
            "High memory usage detected."
        )

    if charging:
        insights.append(
            "Device is currently charging."
        )

    if not insights:
        insights.append(
            "System operating normally."
        )

    return insights