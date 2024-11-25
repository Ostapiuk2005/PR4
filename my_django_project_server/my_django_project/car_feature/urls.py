from django.urls import path
from car_feature.Api.views import CarFeatureList, CarFeatureRetrieve, CarFeatureCreate, CarFeatureUpdate, CarFeatureDestroy



urlpatterns = [
    path('v1/car_feature/', CarFeatureList.as_view(), name='car_feature-list'),
    path('v1/car_feature/<int:pk>/', CarFeatureRetrieve.as_view(), name='car_feature-detail'),
    path('v1/car_feature/create/', CarFeatureCreate.as_view(), name='car_feature-create'),
    path('v1/car_feature/<int:pk>/update/', CarFeatureUpdate.as_view(), name='car_feature-update'),
    path('v1/car_feature/<int:pk>/delete/', CarFeatureDestroy.as_view(), name='car_feature-destroy'),
] 
