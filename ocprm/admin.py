from django.contrib import admin

# Register your models here.

# =============================
# Added by developer after this
# =============================

from .models import Project, StartProjectRequest
from .models import ProjectUserContext

class ProjectUserContextInline(admin.TabularInline):
    """Class for through model."""

    model = ProjectUserContext
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    """Class for project model."""

    inlines = (ProjectUserContextInline,)

admin.site.register(Project, ProjectAdmin)
admin.site.register(StartProjectRequest)

