from django.contrib import admin
from booking.models.booking import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass