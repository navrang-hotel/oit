from django.contrib import admin

# Register your models here.

# =============================
# Added by developer after this
# =============================

from .models import Project

admin.site.register(Project)

