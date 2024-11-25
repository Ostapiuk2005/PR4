from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    year = models.IntegerField(max_length=4)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.model