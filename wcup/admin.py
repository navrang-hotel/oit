from django.contrib import admin

# Register your models here.

# ==============================
# Addeed by developer after this
# ==============================

from .models import Player, Team, Group

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Group)

