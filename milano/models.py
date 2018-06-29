from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

class Dealer(models.Model):
    """Model class for dealer model."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """String repreesntation of object."""

        return self.name

