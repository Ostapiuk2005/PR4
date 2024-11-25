from django.db import models
from car.models.car import Car


class CarFeature(models.Model):
    feature_name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)


    def __str__(self):
        return self.feature_name