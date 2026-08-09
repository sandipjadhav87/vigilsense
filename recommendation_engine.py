def get_recommendation(weather):
    wind = weather["wind_speed"]
    rain = weather["rainfall"]
    humidity = weather["humidity"]
    storm = weather["storm"]

    if storm:
        return {
            "level": "LOW",
            "action": "Reduce sensor sensitivity by 30%"
        }

    if wind > 30:
        return {
            "level": "LOW",
            "action": "Reduce sensor sensitivity by 20%"
        }

    if rain > 10:
        return {
            "level": "MEDIUM",
            "action": "Reduce sensor sensitivity by 10%"
        }

    if humidity > 85:
        return {
            "level": "MEDIUM",
            "action": "Monitor sensor performance"
        }

    return {
        "level": "HIGH",
        "action": "Normal operation"
    }
