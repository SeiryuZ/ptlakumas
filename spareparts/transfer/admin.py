from django.contrib import admin
from spareparts.transfer.models import Transfer, TransferItems, TransferItemsDelivery

admin.site.register(Transfer)
admin.site.register(TransferItems)
admin.site.register(TransferItemsDelivery)