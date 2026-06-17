def get_system_status(
    battery,
    cpu,
    ram
):

    score = (
        battery * 0.5
        +
        (100 - cpu) * 0.25
        +
        (100 - ram) * 0.25
    )

    score = round(score)

    if score >= 80:
        status = "Healthy"

    elif score >= 60:
        status = "Warning"

    else:
        status = "Critical"

    return {
        "score": score,
        "status": status
    }