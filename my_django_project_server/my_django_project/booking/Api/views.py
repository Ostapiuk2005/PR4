from rest_framework import generics
from booking.models.booking import Booking
from booking.serializer.booking import BookingSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(summary="отримання списку всіх бронювань")
class BookingList(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

@extend_schema(summary="отримання деталей про конкретне бронювання", description='виводить всі дані про конкретне брогювання')
class BookingRetrieve(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@extend_schema(summary="створення нового бронювання")
class BookingCreate(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@extend_schema(summary="оновлення даних про бронювання")
class BookingUpdate(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@extend_schema(summary="видалення бронювання", description='видаляє бронювання зі списку')
class BookingDestroy(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer