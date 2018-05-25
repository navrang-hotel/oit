from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

from django.contrib.auth.models import User

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

class NepNews(models.Model):
    """Class for NepTest model."""

    title = models.TextField(max_length=500)

    def __str__(self):
        """String representation of object."""

        return self.title

class FTeam(models.Model):
    """Class for FTeam model."""

    pass

class Poll(models.Model):
    """Class for Poll model."""
    
    pass

class Blog(models.Model):
    """Class for blog model."""
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        """String representation of object."""

        return self.title


class BlogEntry(models.Model):
    """Class for blog entry model."""

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        """String representation of object."""

        return self.blog.title + ' : Entry'

class BlogComment(models.Model):
    """Class for blog comment model."""
    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        """String representation of object."""

        return self.blog.title + ' : Comment'
