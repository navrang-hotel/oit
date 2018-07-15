from django.contrib import admin

# Register your models here.

# =============================
# Added by developer after this
# =============================

from .models import ContactMessage, JobVacancy, JobVacancyEntry
from .models import JobVacancyResponsibility, JobVacancyQualification
from .models import IndexPageHeader, IndexPageHeroPara, IndexPageMain, IndexPagePartner
from .models import IndexPageServices, IndexPageServicesEntry
from .models import OITAddress, ContactPageExistingCustomer, ContactPageFollowUs
from .models import ContactPageWriteMessage, ContactPageHeader
from .models import CareersPageHero, CareersPageReasons, CareersPageReasonsEntry
from .models import UserProfile, Subscriber

admin.site.register(ContactMessage)
admin.site.register(JobVacancy)
admin.site.register(JobVacancyEntry)
admin.site.register(JobVacancyResponsibility)
admin.site.register(IndexPageHeader)
admin.site.register(IndexPageHeroPara)
admin.site.register(IndexPageMain)
admin.site.register(IndexPagePartner)
admin.site.register(ContactPageHeader)
admin.site.register(OITAddress)
admin.site.register(ContactPageWriteMessage)
admin.site.register(ContactPageExistingCustomer)
admin.site.register(ContactPageFollowUs)
admin.site.register(CareersPageHero)
admin.site.register(CareersPageReasons)
admin.site.register(CareersPageReasonsEntry)
admin.site.register(UserProfile)
admin.site.register(IndexPageServices)
admin.site.register(IndexPageServicesEntry)
admin.site.register(Subscriber)

