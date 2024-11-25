from django.contrib import admin
from car_feature.models.car_feature import CarFeature


@admin.register(CarFeature)
class CarFeatureAdmin(admin.ModelAdmin):
    pass