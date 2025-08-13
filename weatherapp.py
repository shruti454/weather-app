import requests

API_KEY = "XZel4yyH1iiTEA2Bg3UlBkhimH0D2-JacPcHR_jKX8w"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n📍 Weather in {city_name}, {country}:")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"☁️ Condition: {weather_desc}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬 Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
