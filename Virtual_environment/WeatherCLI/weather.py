#!/usr/bin/env python3
"""
Weather CLI Script - WeatherCLI Project
Uses requests==2.31.0 in its virtual environment
Fetches current weather data from OpenWeatherMap API
"""

import requests
import sys

def get_weather(city):
    """
    Fetch current weather data for a given city
    
    Args:
        city (str): Name of the city to get weather for
        
    Returns:
        dict: Weather data or None if request fails
    """
    # OpenWeatherMap API endpoint (using demo API key for testing)
    # Note: For production use, you should get your own API key from openweathermap.org
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': 'demo',  # Demo API key - limited functionality
        'units': 'metric'  # Get temperature in Celsius
    }
    
    try:
        # Make API request using requests==2.31.0
        print(f"Using requests version: {requests.__version__}")
        response = requests.get(base_url, params=params, timeout=10)
        
        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print("⚠️  Demo API key has limited access. For full functionality, get a free API key from openweathermap.org")
            return None
        else:
            print(f"❌ Error: Unable to fetch weather data (Status code: {response.status_code})")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def display_weather(weather_data, city):
    """
    Display weather information in a user-friendly format
    
    Args:
        weather_data (dict): Weather data from API
        city (str): City name for display
    """
    if not weather_data:
        print(f"❌ Could not retrieve weather data for {city}")
        return
    
    try:
        # Extract temperature and weather condition
        temp = weather_data['main']['temp']
        condition = weather_data['weather'][0]['description'].title()
        
        # Display the result
        print(f"🌤️  Weather in {city.title()}: {temp}°C, {condition}")
        
        # Additional info if available
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        print(f"   Feels like: {feels_like}°C | Humidity: {humidity}%")
        
    except KeyError as e:
        print(f"❌ Error parsing weather data: Missing key {e}")

def main():
    """
    Main function - handles user input and coordinates weather fetching
    """
    print("=== WeatherCLI - Python Virtual Environment Demo ===")
    print("This script uses requests==2.31.0 from its virtual environment\n")
    
    # Get city name from user input
    try:
        city = input("🏙️  Enter city name: ").strip()
        
        if not city:
            print("❌ Please enter a valid city name")
            return
        
        print(f"🔍 Fetching weather data for {city}...")
        
        # Fetch and display weather data
        weather_data = get_weather(city)
        display_weather(weather_data, city)
        
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()