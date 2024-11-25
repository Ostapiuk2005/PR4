from rest_framework import serializers
from car_feature.models.car_feature import CarFeature


class CarFeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarFeature
        fields = ['id', 'feature_name', 'car_id']