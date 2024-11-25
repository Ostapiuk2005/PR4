from rest_framework import serializers
from booking.models.booking import Booking


class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ['id', 'user_id', 'car_id', 'start_date', 'end_date', 'total_price', 'status']
