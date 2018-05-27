from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

class Customer(models.Model):
    """Model class for customer."""

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        """String represenation of object."""

        return self.name

class Room(models.Model):
    """Model class for room."""

    name = models.CharField(max_length=20)
    room_type = models.CharField(max_length=20)

    def __str__(self):
        """String represenation of object."""

        return self.name

class Booking(models.Model):
    """Model class for booking."""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_status = models.CharField(max_length=10)

    def __str__(self):
        """String represenation of object."""

        return 'Booking o'

