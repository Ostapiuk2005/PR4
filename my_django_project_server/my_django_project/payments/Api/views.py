from rest_framework import generics
from payments.models.payment import Payment
from payments.serializer.payments import PaymentSerializer
from drf_spectacular.utils import extend_schema



@extend_schema(summary="отримання списку всіх оплат")
class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    

@extend_schema(summary="отримання деталей про конкретну оплат")
class PaymentRetrieve(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@extend_schema(summary="створення нової оплати", description='створює нову оплату')
class PaymentCreate(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@extend_schema(summary="оновлення даних про оплату")
class PaymentUpdate(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    

@extend_schema(summary="видалення оплати")
class PaymentDestroy(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
