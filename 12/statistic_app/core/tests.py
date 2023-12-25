from django.test import TestCase
from core.models import City, Weather
from core.services import parse_weather_from_api


class ParserTestCase(TestCase):
    def setUp(self) -> None:
        self.city = 'Moscow'
        self.bad_city = 'unknown_city'

    def test_parse_weather_from_api_success(self):
        data = parse_weather_from_api(self.city)
        city = City.objects.get(name=self.city)
        self.assertTrue(data)
        self.assertTrue(City.objects.filter(name=self.city).exists())
        self.assertTrue(Weather.objects.filter(city=city).exists())

    def test_parse_weather_from_api_fail(self):
        data = parse_weather_from_api(self.bad_city)
        self.assertFalse(data)
        self.assertFalse(City.objects.filter(name=self.bad_city).exists())
