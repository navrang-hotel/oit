from django.contrib import admin

# Register your models here.

# =============================
# Added by developer after this
# =============================

from .models import Room, Booking, Customer

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Customer)

