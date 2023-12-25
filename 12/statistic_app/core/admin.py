from django.contrib import admin

from core.models import Weather, City


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
