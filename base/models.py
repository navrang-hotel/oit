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

# ===
# CMS
# ===


# ==========
# ==========
# Index Page
# ==========
# ==========


# =================    
# Index Page header    
# =================    

class IndexPageHeader(models.Model):
    """Model class for index page header."""

    title = models.CharField(max_length=100)

    def __str__(self):
        """String representation of object."""

        return self.title

# ====================    
# Index Page Hero para    
# ====================    

class IndexPageHeroPara(models.Model):
    """Model class for index page hero paragraph."""

    body = models.TextField(max_length=500)

    def __str__(self):
        """String representation of object."""

        return self.body

# ===============    
# Index Page Main
# ===============    

class IndexPageMain(models.Model):
    """Model class for index page main section."""

    header = models.CharField(max_length=50)

    def __str__(self):
        """String representation of object."""

        return self.header

# ===============    
# Index Page Main
# ===============    

class IndexPagePartner(models.Model):
    """Model class for index page partner section."""

    header = models.CharField(max_length=50)

    def __str__(self):
        """String representation of object."""

        return self.header


# ============
# ============
# Contact Page
# ============
# ============


# ===================
# Contact Page header
# ===================

class ContactPageHeader(models.Model):
    """Model class for Contact page header."""

    header = models.CharField(max_length=100)

	
    def __str__(self):
        """String representation of object."""

        return self.header

# ===========
# OIT Address
# ===========

class OITAddress(models.Model):
    """Model class for OIT address."""

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)

	
    def __str__(self):
        """String representation of object."""

        return self.name

# ==========================
# Contact page Write message
# ==========================

class ContactPageWriteMessage(models.Model):
    """Model class for contact page write message section."""

    header = models.CharField(max_length=100)
    body = models.TextField(max_length=200)

    def __str__(self):
        """String representation of object."""

        return self.header
    
# ==============================
# Contact page Existing Customer
# ==============================

class ContactPageExistingCustomer(models.Model):
    """Model class for contact page existing customer section."""

    header1 = models.CharField(max_length=100)
    header2 = models.CharField(max_length=100)
    btn_bs_class = models.CharField(max_length=20)

    def __str__(self):
        """String representation of object."""

        return self.header1

# ======================
# Contact page Follow us
# ======================

class ContactPageFollowUs(models.Model):
    """Model class for contact page follow us section."""

    header = models.CharField(max_length=100)

    def __str__(self):
        """String representation of object."""

        return self.header


# ============
# ============
# Careers Page
# ============
# ============


# =================
# Careers page hero
# =================

class CareersPageHero(models.Model):
    """Model class for careers page hero section."""    

    header = models.CharField(max_length=100)
    body = models.TextField(max_length=500)

    def __str__(self):
        """String representation of object."""

        return self.header

# ====================
# Careers page reasons
# ====================

class CareersPageReasons(models.Model):
    """Model class for careers page reasons section."""    

    header = models.CharField(max_length=100)

    def __str__(self):
        """String representation of object."""

        return self.header

class CareersPageReasonsEntry(models.Model):
    """Model class for careers page reasons entry."""    

    careers_page_reasons = models.ForeignKey(CareersPageReasons, on_delete=models.CASCADE)
    order = models.IntegerField()
    header = models.CharField(max_length=100)
    icon_bs_class = models.CharField(max_length=50)
    body = models.TextField(max_length=500)

    def __str__(self):
        """String representation of object."""

        return self.header

    class Meta:

        ordering = ['order',]

# ============
# User profile
# ============

class UserProfile(models.Model):
    """Class for user profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200)
    phone_num = models.TextField(max_length=20)

    def __str__(self):
        """String representation of object."""

        return self.user.username
    
class IndexPageServices(models.Model):
    """Class for index page services cms."""
    
    header = models.CharField(max_length=20)
    lpara = models.TextField(max_length=200)

    def __str__(self):
        """String representation of object."""

        return self.header

class IndexPageServicesEntry(models.Model):
    """Model class for index page services entry."""    

    index_page_services = models.ForeignKey(IndexPageServices, on_delete=models.CASCADE)
    order = models.IntegerField()
    header = models.CharField(max_length=100)
    icon_bs_class = models.CharField(max_length=50)
    body = models.TextField(max_length=500)

    def __str__(self):
        """String representation of object."""

        return self.header

    class Meta:

        ordering = ['order',]

class Subscriber(models.Model):
    """Model class for subscriber."""

    email = models.EmailField()

    def __str__(self):
        """String representation of object."""

        return self.email

