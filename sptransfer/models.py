from django.db import models
from sp_spareparts.models import StockSpareParts

# Create your models here.

class Transfer(models.Model):
	number = models.CharField (max_length=20, unique=True)
	request_approv = models.BooleanField()
	request_reject = models.BooleanField()
	cancel_flag = models.BooleanField()
	closed_flag = models.BooleanField()
	memo = models.TextField()

class TransferItems(models.Model):
	transfer = models.ForeignKey (Transfer, on_delete=models.PROTECT)
	origin = models.ForeignKey(StockSpareParts, 
		on_delete=models.PROTECT, related_name='origin')
	destination = models.ForeignKey(StockSpareParts, 
		on_delete=models.PROTECT, related_name='destination')
	requested_quantity = models.PositiveSmallIntegerField()
	approved_quantity = models.PositiveSmallIntegerField(blank=True, null=True)
	memo = models.TextField(blank=True, null=True)

class TransferItemsDelivery(models.Model):
	transfer_items = models.ForeignKey(TransferItems, on_delete=models.PROTECT)
	delivery_date = models.DateField()
	delivered_quantity = models.PositiveSmallIntegerField()
	memo = models.TextField(blank=True, null=True)
	

