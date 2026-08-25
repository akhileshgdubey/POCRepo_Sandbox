# test_weather.py

from weather_agent.tools import get_weather


# Example coordinates for testing
latitude = 22.3072
longitude = 73.1812


# Call the weather function
weather_data = get_weather(
    latitude=latitude,
    longitude=longitude
)


# Print the result
print("Weather API Response:")
print(weather_data)