from django.db import models
from sp_spareparts.models import StockSpareParts
from django.db.models.signals import post_save, pre_delete
from logs.signals import add_spareparts_logs, delete_spareparts_logs

# Create your models here.

class Transfer(models.Model):
	origin = models.ForeignKey(StockSpareParts, 
		on_delete=models.PROTECT, related_name='origin')
	destination = models.ForeignKey(StockSpareParts, 
		on_delete=models.PROTECT, related_name='destination')
	number = models.CharField (max_length=20, unique=True)
	request_approv = models.BooleanField()
	request_reject = models.BooleanField()
	cancel_flag = models.BooleanField()
	closed_flag = models.BooleanField()
	memo = models.TextField()

class TransferItems(models.Model):
	transfer = models.ForeignKey (Transfer, on_delete=models.PROTECT)
	requested_quantity = models.PositiveSmallIntegerField()
	approved_quantity = models.PositiveSmallIntegerField(blank=True, null=True)
	memo = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "Transfer Item"

class TransferItemsDelivery(models.Model):
	transfer_items = models.ForeignKey(TransferItems, on_delete=models.PROTECT)
	delivery_date = models.DateField()
	delivered_quantity = models.PositiveSmallIntegerField()
	memo = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "Deliverie"
	
post_save.connect(add_spareparts_logs, sender=Transfer)
pre_delete.connect(delete_spareparts_logs, sender=Transfer)

post_save.connect(add_spareparts_logs, sender=TransferItems)
pre_delete.connect(delete_spareparts_logs, sender=TransferItems)