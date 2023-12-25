from rest_framework import serializers

from core.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')

    class Meta:
        model = Weather
        fields = '__all__'
