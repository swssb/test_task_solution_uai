from django.db import models


class City(models.Model):
    name = models.CharField(max_length=55, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    temperature = models.FloatField(verbose_name='Температура')
    feels_like = models.FloatField(verbose_name='Ощущается как')
    measured_at = models.DateTimeField(auto_now_add=True, verbose_name='Время измерения')

    class Meta:
        verbose_name = 'Погода'
        verbose_name_plural = 'Погода'

    def save(self, *args, **kwargs):
        self.temperature = round(float(self.temperature) - 273.15, 1)
        self.feels_like = round(float(self.feels_like) - 273.15, 1)
        super().save(*args, **kwargs)
