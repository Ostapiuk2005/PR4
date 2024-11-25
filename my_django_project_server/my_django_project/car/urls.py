from django.urls import path
from car.Api.views import CarList, CarRetrieve, CarCreate, CarUpdate, CarDestroy



urlpatterns = [
    path('v1/cars/', CarList.as_view(), name='cars-list'),
    path('v1/cars/<int:pk>/', CarRetrieve.as_view(), name='cars-detail'),
    path('v1/cars/create/', CarCreate.as_view(), name='cars-create'),
    path('v1/cars/<int:pk>/update/', CarUpdate.as_view(), name='cars-update'),
    path('v1/cars/<int:pk>/delete/', CarDestroy.as_view(), name='cars-destroy'),
] 
