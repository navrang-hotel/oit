from django.contrib import admin

# Register your models here.

# =============================
# Added by developer after this
# =============================

from .models import Project, StartProjectRequest

admin.site.register(Project)
admin.site.register(StartProjectRequest)

