from flask import Flask, jsonify
import requests
import os
from recommendation_engine import get_recommendation

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")
CITY = os.getenv("CITY", "Shirdi")

@app.route("/")
def home():
    return "VigilSense API Running"

@app.route("/api/recommend")
def recommend():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    weather = {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"] * 3.6,  # m/s to km/h
        "rainfall": data.get("rain", {}).get("1h", 0),
        "storm": any(w["id"] // 100 == 2 for w in data["weather"])
    }

    recommendation = get_recommendation(weather)

    return jsonify({
        "weather": weather,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run(debug=True)
