from django.contrib import admin

# Register your models here.
# =============================
# Added by developer after this
# =============================


from .models import Dealer, Product, Kart, Cartism

admin.site.register(Dealer)
admin.site.register(Product)
admin.site.register(Kart)
admin.site.register(Cartism)

