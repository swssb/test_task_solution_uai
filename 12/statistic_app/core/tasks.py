from celery import shared_task

from core.services import parse_weather_from_api


@shared_task()
def update_weather() -> str:
    cities = ('Moscow', 'Novosibirsk', 'Omsk', 'Kazan', 'Tomsk')
    for city in cities:
        parse_weather_from_api(city)
    return 'Weather Updated'
