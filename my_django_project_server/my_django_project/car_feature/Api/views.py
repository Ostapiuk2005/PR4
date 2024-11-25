from rest_framework import generics
from car_feature.models.car_feature import CarFeature
from car_feature.serializer.car_feature import CarFeatureSerializer
from drf_spectacular.utils import extend_schema


    
@extend_schema(summary="отримання списку всіх характеристик автомобілів")
class CarFeatureList(generics.ListAPIView):
    queryset = CarFeature.objects.all()
    serializer_class = CarFeatureSerializer
    

@extend_schema(summary="отримання деталей про конкретну характеристику", description='виводить всі дані про конкретну характеристику')
class CarFeatureRetrieve(generics.RetrieveAPIView):
    queryset = CarFeature.objects.all()
    serializer_class = CarFeatureSerializer


@extend_schema(summary="створення нової характеристики автомобіля")
class CarFeatureCreate(generics.CreateAPIView):
    queryset = CarFeature.objects.all()
    serializer_class = CarFeatureSerializer


@extend_schema(summary="оновлення даних про характеристику автомобіля")
class CarFeatureUpdate(generics.UpdateAPIView):
    queryset = CarFeature.objects.all()
    serializer_class = CarFeatureSerializer
    

@extend_schema(summary="видалення характеристики автомобіля", description='видаляє характеристику автомобіля зі списку')
class CarFeatureDestroy(generics.DestroyAPIView):
    queryset = CarFeature.objects.all()
    serializer_class = CarFeatureSerializer