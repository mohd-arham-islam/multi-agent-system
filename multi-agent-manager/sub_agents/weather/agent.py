import os
import requests
from dotenv import load_dotenv
from google.adk.agents import Agent

# Load environment variables from .env file
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_current_weather(location: str) -> dict:
    """
    Fetch current weather for a given location.

    Args:
        location (str): City or coordinates (e.g., "New York" or "37.7749,-122.4194")

    Returns:
        dict: Current weather data or error
    """
    if not WEATHER_API_KEY:
        return {"status": "error", "error": "Missing API key"}
    
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": WEATHER_API_KEY,
        "q": location
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "status": "success",
            "location": data.get("location", {}).get("name"),
            "country": data.get("location", {}).get("country"),
            "temperature_c": data.get("current", {}).get("temp_c"),
            "condition": data.get("current", {}).get("condition", {}).get("text"),
            "humidity": data.get("current", {}).get("humidity"),
            "wind_kph": data.get("current", {}).get("wind_kph")
        }

    except Exception as e:
        return {"status": "error", "error": str(e)}

def get_weather_forecast(location: str, days: int = 3) -> dict:
    """
    Fetch future weather forecast for a given location.

    Args:
        location (str): City or coordinates
        days (int): Number of days (1 to 10)

    Returns:
        dict: Weather forecast data or error
    """
    if not WEATHER_API_KEY:
        return {"status": "error", "error": "Missing API key"}
    
    if days < 1 or days > 10:
        return {"status": "error", "error": "Forecast days must be between 1 and 10"}

    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": WEATHER_API_KEY,
        "q": location,
        "days": days
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        forecasts = []
        for day in data.get("forecast", {}).get("forecastday", []):
            forecasts.append({
                "date": day["date"],
                "avg_temp_c": day["day"]["avgtemp_c"],
                "condition": day["day"]["condition"]["text"],
                "max_wind_kph": day["day"]["maxwind_kph"],
                "chance_of_rain": day["day"].get("daily_chance_of_rain")
            })

        return {
            "status": "success",
            "location": data.get("location", {}).get("name"),
            "country": data.get("location", {}).get("country"),
            "forecast": forecasts
        }

    except Exception as e:
        return {"status": "error", "error": str(e)}

weather_agent = Agent(
    name="weather",
    model="gemini-2.0-flash",
    description="Provides current weather information and multi-day forecasts for any global location.",
    instruction="""
You are a weather expert. Use the tools provided to answer weather-related queries such as:

- What is the weather like in a city right now?
- Should I carry an umbrella tomorrow in Paris?
- What is the temperature forecast for the next 3 days in Tokyo?

Always ask for the location if it's missing. For forecasts, specify the number of days if not given (default to 3).

Use the `get_current_weather` tool for live conditions and `get_weather_forecast` for future forecasts.
""",
    tools=[get_current_weather, get_weather_forecast]
)