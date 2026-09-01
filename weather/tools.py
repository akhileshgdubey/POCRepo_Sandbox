# weather_agent/tools.py

import requests


def get_location_coordinates(location: str) -> dict:
    """
    Find the latitude and longitude of a location.

    Args:
        location: City, town, or other location name.

    Returns:
        A dictionary containing the location details
        and coordinates.
    """

    # Open-Meteo Geocoding API
    url = "https://geocoding-api.open-meteo.com/v1/search"

    # Parameters for the geocoding request
    params = {
        "name": location,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    try:
        # Send GET request to Open-Meteo Geocoding API
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Convert JSON response into Python dictionary
        data = response.json()

        # Get the search results
        results = data.get("results", [])

        # Check whether a location was found
        if not results:
            return {
                "status": "error",
                "message": f"Location '{location}' could not be found.",
            }

        # Take the first matching location
        result = results[0]

        # Return clean location information
        return {
            "status": "success",
            "location": {
                "name": result.get("name"),
                "country": result.get("country"),
                "latitude": result.get("latitude"),
                "longitude": result.get("longitude"),
                "timezone": result.get("timezone"),
            },
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"Unable to find location: {str(e)}",
        }


def get_weather(latitude: float, longitude: float) -> dict:
    """
    Get current weather information for a location.

    Args:
        latitude: Latitude of the location.
        longitude: Longitude of the location.

    Returns:
        A dictionary containing the weather information.
    """

    # Open-Meteo forecast API endpoint
    url = "https://api.open-meteo.com/v1/forecast"

    # Parameters sent to Open-Meteo
    params = {
        "latitude": latitude,
        "longitude": longitude,

        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m"
        ),

        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "auto",
    }

    try:
        # Send GET request to Open-Meteo
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        # Raise an exception if the API returns an HTTP error
        response.raise_for_status()

        # Convert JSON response into Python dictionary
        data = response.json()

        # Return a clean response
        return {
            "status": "success",

            "location": {
                "latitude": latitude,
                "longitude": longitude,
            },

            "weather": data.get("current", {}),
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"Unable to retrieve weather data: {str(e)}",
        }