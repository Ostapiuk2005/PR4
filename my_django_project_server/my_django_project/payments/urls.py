from django.urls import path
from payments.Api.views import PaymentList, PaymentRetrieve, PaymentCreate, PaymentUpdate, PaymentDestroy



urlpatterns = [
    path('v1/payments/', PaymentList.as_view(), name='payments-list'),
    path('v1/payments/<int:pk>/', PaymentRetrieve.as_view(), name='payments-detail'),
    path('v1/payments/create/', PaymentCreate.as_view(), name='payments-create'),
    path('v1/payments/<int:pk>/update/', PaymentUpdate.as_view(), name='payments-update'),
    path('v1/payments/<int:pk>/delete/', PaymentDestroy.as_view(), name='payments-destroy'),
] 
