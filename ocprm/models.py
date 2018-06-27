from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

from django.contrib.auth.models import User
from django.utils import timezone

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

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=STATUS)
    start_date = models.DateField()
    end_date = models.DateField()
    live_url = models.CharField(max_length=100)
    client_poc = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_poc')
    vendor_poc = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor_poc')
    actors = models.ManyToManyField(User, through='ProjectUserContext')

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


# ==============
# Junction table
# ==============

# TODO: Need to rename this class (with a suitable name hopefully).
class ProjectUserContext(models.Model):
    """Model class for project-x-user junction table.

    There is a many-to-many relationship between project and user through 
    context.
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)

    def __str__(self):
        """String representation of the object."""

        return self.project.name + ' <-> ' + self.user.username
    

# ====
# Task
# ====

class ProjectTask(models.Model):
    """Class for project task model."""

    STATUS = (
        ('N', 'New',),
        ('O', 'Open',),
        ('I', 'InProgress',),
        ('H', 'OnHold',),
        ('C', 'Complete',),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS)
    start_date = models.DateField()
    target_end_date = models.DateField()
    actual_end_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_owner')
    raiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_raiser')
    
    def __str__(self):
        """String representation of object."""
        
        return self.project.name + self.name

# =======
# Comment
# =======

class ProjectComment(models.Model):
    """Class for project comment model."""

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    write_dtime = models.DateTimeField(default=timezone.now)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """String representation of object."""
        
        return self.project.name + self.commentor.username

    class Meta:
        ordering = ['-write_dtime']

# ==================
# Get support ticket
# ==================

class GetSupportTicket(models.Model):
    """Class for get support ticket model."""

    STATUS = (
        ('N', 'New',),
        ('O', 'Open',),
        ('F', 'Fixed',),
        ('R', 'Re-test',),
        ('C', 'Closed',),
    )

    RCA = (
        ('C', 'Code',),
        ('D', 'Design',),
        ('U', 'User-error',),
        ('E', 'Environment',),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    raised_date = models.DateTimeField(default=timezone.now)
    closed_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS)
    rca = models.CharField(max_length=1, choices=RCA, null=True, blank=True)

    def __str__(self):
        """String representation of object."""
        
        return  '[' + str(self.id) + '] ' + self.title

