import requests
from rest_framework import status

from core.models import Weather, City
from statistic_app import settings


def parse_weather_from_api(city: str) -> str:
    url = settings.WEATHER_URL
    api_key = settings.WEATHER_API_KEY
    response = requests.get(url, params={'q': f'{city},Russia', 'appid': api_key})

    if response.status_code == status.HTTP_200_OK:
        data = response.json()
        city = data['name']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        create_objects(city, temperature, feels_like)
        return data
    else:
        print(f"Parsing failed. Status code: {response.status_code}")


def create_objects(city: str, temperature: str, feels_like: str):
    city_obj, _ = City.objects.get_or_create(name=city)
    Weather.objects.create(city=city_obj, temperature=temperature, feels_like=feels_like)
