from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

from datetime import datetime

from django.contrib.auth.models import User


# ===============
# Project
# ===============

class Project(models.Model):
    """Model class for project."""

    STATUS = (
        ('D', 'Design',),
        ('V', 'Develop',),
        ('M', 'Maintainance',),
    )

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    live_url = models.CharField(max_length=100)

    def __str__(self):
        """String representation of object."""
        
        return self.name

# ===============
# Contact Message
# ===============

class ContactMessage(models.Model):
    """Class for contact message model."""

    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    date_time = models.DateTimeField(default=datetime.now)

    STATUS = (
        ('N', 'New',),
        ('P', 'Progress',),
        ('R', 'Replied',),
    )

    status = models.CharField(max_length=1, choices=STATUS, default='N')

    def __str__(self):
        """String representation of the model."""

        return self.sender_name

