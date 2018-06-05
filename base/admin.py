from django.contrib import admin

# Register your models here.

# =============================
# Added by developer after this
# =============================

from .models import ContactMessage, JobVacancy, JobVacancyEntry
from .models import JobVacancyResponsibility, JobVacancyQualification
from .models import IndexPageHeader, IndexPageHeroPara
from .models import OITAddress, ContactPageExistingCustomer, ContactPageFollowUs
from .models import ContactPageWriteMessage, ContactPageHeader

admin.site.register(ContactMessage)
admin.site.register(JobVacancy)
admin.site.register(JobVacancyEntry)
admin.site.register(JobVacancyResponsibility)
admin.site.register(IndexPageHeader)
admin.site.register(IndexPageHeroPara)
admin.site.register(ContactPageHeader)
admin.site.register(OITAddress)
admin.site.register(ContactPageWriteMessage)
admin.site.register(ContactPageExistingCustomer)
admin.site.register(ContactPageFollowUs)

