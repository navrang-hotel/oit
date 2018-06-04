from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

from datetime import datetime

from django.contrib.auth.models import User

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

# ===========
# Job Vacancy
# ===========

class JobVacancy(models.Model):
    """Class for job vacancy model."""

    JOB_TYPE = (
        ('I', 'Internship',),
        ('C', 'Contract',),
        ('F', 'Fulltime',),
    )
    title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=1, choices=JOB_TYPE)

    def __str__(self):
        """String representation of the model."""

        return self.title

class JobVacancyResponsibility(models.Model):
    """Class for job vacancy responsibility model."""

    order = models.IntegerField()
    job_vacancy = models.ForeignKey(JobVacancy, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    
    def __str__(self):
        """String representation of the model."""

        return self.body + ' JobVacResp'

class JobVacancyQualification(models.Model):
    """Class for job vacancy qualification model."""

    order = models.IntegerField()
    job_vacancy = models.ForeignKey(JobVacancy, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    
    def __str__(self):
        """String representation of the model."""

        return self.body + ' JobVacQual'

    class Meta:

        ordering = ['order',]


class JobVacancyEntry(models.Model):
    """Class for job vacancy entry model."""

    order = models.IntegerField()
    job_vacancy = models.ForeignKey(JobVacancy, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        """String representation of the model."""

        return self.title

    class Meta:

        ordering = ['order',]

    
