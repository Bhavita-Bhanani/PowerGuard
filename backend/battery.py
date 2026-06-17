import psutil


def get_battery_info():

    battery = psutil.sensors_battery()

    if battery is None:
        return {
            "available": False
        }

    seconds_left = battery.secsleft

    if seconds_left == -2:
        time_remaining = "Charging"

    elif seconds_left == -1:
        time_remaining = "Calculating"

    else:

        hours = seconds_left // 3600
        minutes = (seconds_left % 3600) // 60

        time_remaining = f"{hours}h {minutes}m"

    return {
        "available": True,
        "percent": battery.percent,
        "charging": battery.power_plugged,
        "time_remaining": time_remaining
    }