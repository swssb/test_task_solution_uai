import datetime

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import Weather
from core.serializers import WeatherSerializer


class WeatherStatisticView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Weather.objects.filter(measured_at__date=datetime.date.today())
    serializer_class = WeatherSerializer
