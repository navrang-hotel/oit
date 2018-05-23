from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

class Group(models.Model):
    """Class for Group model."""

    name = models.CharField(max_length=1)

    def __str__(self):
        """String representation of object."""

        return self.name

class Team(models.Model):
    """Class for team model."""

    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of object."""

        return self.name


class Player(models.Model):
    """Class for player model."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, default=1, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of object."""

        return self.first_name + ' ' + self.last_name

