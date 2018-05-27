from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

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

