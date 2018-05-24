from django.contrib import admin

# Register your models here.

# ==============================
# Addeed by developer after this
# ==============================

from .models import Player, Team, Group, NepNews
from .models import Blog, BlogEntry, BlogComment

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Group)
admin.site.register(NepNews)

admin.site.register(Blog)
admin.site.register(BlogEntry)
admin.site.register(BlogComment)

