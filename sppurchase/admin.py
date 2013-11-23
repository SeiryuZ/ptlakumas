from django.contrib import admin
from sppurchase.models import Purchase, PurchaseItems, PurchaseItemsDelivery

admin.site.register(Purchase)
admin.site.register(PurchaseItems)
admin.site.register(PurchaseItemsDelivery)