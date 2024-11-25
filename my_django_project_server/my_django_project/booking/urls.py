from django.urls import path
from booking.Api.views import BookingList, BookingRetrieve, BookingCreate, BookingUpdate, BookingDestroy



urlpatterns = [
    path('v1/bookings/', BookingList.as_view(), name='bookings-list'),
    path('v1/bookings/<int:pk>/', BookingRetrieve.as_view(), name='bookings-detail'),
    path('v1/bookings/create/', BookingCreate.as_view(), name='bookings-create'),
    path('v1/bookings/<int:pk>/update/', BookingUpdate.as_view(), name='bookings-update'),
    path('v1/bookings/<int:pk>/delete/', BookingDestroy.as_view(), name='bookings-destroy'),
] 
