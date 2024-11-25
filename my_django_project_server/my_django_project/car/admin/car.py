from django.contrib import admin
from car.models.car import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass