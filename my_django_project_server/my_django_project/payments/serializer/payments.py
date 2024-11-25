from rest_framework import serializers
from payments.models.payment import Payment



class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = ['id', 'booking_id', 'payment_data', 'amount', 'payment_method', 'status']
