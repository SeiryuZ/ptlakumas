from django.contrib import admin
from spareparts.purchase.models import Purchase, PurchaseItems, PurchaseItemsDelivery

admin.site.register(Purchase)
admin.site.register(PurchaseItems)
admin.site.register(PurchaseItemsDelivery)