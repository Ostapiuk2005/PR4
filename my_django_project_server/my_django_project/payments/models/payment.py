from django.db import models
from booking.models.booking import Booking



class Payment(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_data = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.payment_data