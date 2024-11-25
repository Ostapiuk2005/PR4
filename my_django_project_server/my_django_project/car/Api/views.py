from rest_framework import viewsets, generics
from car.models.car import Car
from car.serializer.car import CarSerializer
from drf_spectacular.utils import extend_schema


    
@extend_schema(summary="отримання списку всіх машин")
class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    

@extend_schema(summary="отримання деталей про конкретну машину", description='виводить всі дані про конкретну машину')
class CarRetrieve(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


@extend_schema(summary="створення нової машини")
class CarCreate(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


@extend_schema(summary="оновлення даних про машину")
class CarUpdate(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    

@extend_schema(summary="видалення машини", description='видаляє машину зі списку')
class CarDestroy(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer