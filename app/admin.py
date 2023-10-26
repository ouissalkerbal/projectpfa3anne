#app/admin.py
from django.contrib import admin
from .models import PurchaseOrder, TypeDeConnecteurs, TypeDeCable

admin.site.register(PurchaseOrder)
admin.site.register(TypeDeConnecteurs)
admin.site.register(TypeDeCable)
admin.site.site_header = "Your Custom Site Header"