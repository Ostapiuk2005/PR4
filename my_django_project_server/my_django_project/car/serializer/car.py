from rest_framework import serializers
from car.models.car import Car


class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price_per_day']