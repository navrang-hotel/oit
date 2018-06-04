from django.contrib import admin

# Register your models here.

# =============================
# Added by developer after this
# =============================

from .models import ContactMessage, JobVacancy, JobVacancyEntry
from .models import JobVacancyResponsibility, JobVacancyQualification
from .models import IndexPageHeader, IndexPageHeroPara

admin.site.register(ContactMessage)
admin.site.register(JobVacancy)
admin.site.register(JobVacancyEntry)
admin.site.register(JobVacancyResponsibility)
admin.site.register(IndexPageHeader)
admin.site.register(IndexPageHeroPara)

