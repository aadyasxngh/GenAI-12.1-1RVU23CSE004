import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# Weather tool
def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        data = response.json()

        # ✅ FIXED: Check for API errors explicitly
        if data.get("cod") != 200:
            return f"⚠️ Weather data unavailable: {data.get('message', 'Unknown error')}"

        description = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        return (
            f"Current weather in {city}: {description}\n"
            f"Temperature: {temp}°C (Feels like {feels_like}°C)\n"
            f"Humidity: {humidity}%"
        )

    except requests.exceptions.Timeout:
        return "⚠️ Weather API timed out. Please try again."
    except Exception as e:
        return f"⚠️ Weather data not available: {str(e)}"


# Flight tool (simulated for lab)
def get_flights(city):
    # ✅ FIXED: Returns a formatted string instead of a list
    flights = [
        f"Bangalore → {city} | Air India   | Economy ₹4,500 | Business ₹12,000",
        f"Bangalore → {city} | IndiGo      | Economy ₹3,800 | Business ₹10,500",
        f"Bangalore → {city} | Emirates    | Economy ₹6,200 | Business ₹18,000",
    ]
    return "\n".join(f"- {f}" for f in flights)


# Hotel tool (simulated)
def get_hotels(city):
    # ✅ FIXED: Returns a formatted string instead of a list
    hotels = [
        f"Grand Hotel {city}         | ⭐⭐⭐⭐⭐ | ₹8,000/night | Pool, Spa, Restaurant",
        f"{city} Palace Hotel        | ⭐⭐⭐⭐   | ₹5,500/night | Free WiFi, Breakfast",
        f"Central {city} Residency   | ⭐⭐⭐     | ₹2,800/night | Budget-friendly, City Center",
    ]
    return "\n".join(f"- {h}" for h in hotels)