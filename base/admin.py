from django.contrib import admin

# Register your models here.

# =============================
# Added by developer after this
# =============================

from .models import ContactMessage

admin.site.register(ContactMessage)

