from django.db import models
from users.models.user import CustomUser
from car.models.car import Car



class Booking(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add = True)
    end_date = models.DateField(auto_now_add = True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.total_price