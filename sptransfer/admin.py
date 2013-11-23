from django.contrib import admin
from sptransfer.models import Transfer, TransferItems, TransferItemsDelivery

admin.site.register(Transfer)
admin.site.register(TransferItems)
admin.site.register(TransferItemsDelivery)