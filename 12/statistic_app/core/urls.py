from django.urls import path

from .views import WeatherStatisticView

urlpatterns = [
    path('weather/', WeatherStatisticView.as_view())
]