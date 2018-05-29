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

# =====================
# Start Project request
# =====================

class StartProjectRequest(models.Model):
    """Model class for start project request."""

    STATUS = (
        ('P', 'Pending',),
        ('D', 'Denied',),
        ('H', 'On-Hold',),
        ('A', 'Approved',),
    )

    PROJECT_TYPE = (
        ('P', 'Personal',),
        ('B', 'Business',),
    )


    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS)
    project_type = models.CharField(max_length=1, choices=PROJECT_TYPE)
    description = models.TextField()

    def __str__(self):
        """String representation of object."""
        
        return self.email

