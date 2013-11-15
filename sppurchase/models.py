from django.db import models
from sp_spareparts.models import StockSpareParts
from django.db.models.signals import post_save, pre_delete
from logs.signals import add_spareparts_logs, delete_spareparts_logs

# Create your models here.

class Purchase(models.Model):
	request_number = models.CharField('Purchase Request Number', 
		max_length=20, unique=True)
	request_approval = models.BooleanField()
	request_reject = models.BooleanField()
	order_number = models.CharField('Purchase Order Number',
		max_length=20, unique=True, null=True, blank=True)
	cancel_flag = models.BooleanField()
	closed_flag = models.BooleanField()
	memo = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.request_number

class PurchaseItems(models.Model):
	purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT)
	stock_spare_parts = models.ForeignKey(StockSpareParts, 
		on_delete=models.PROTECT)
	requested_quantity = models.PositiveSmallIntegerField()
	unit_price = models.IntegerField(null=True, blank=True)
	additional_cost = models.IntegerField(null=True, blank=True)
	approved_quantity = models.PositiveSmallIntegerField(blank=True, null=True)
	memo = models.TextField(blank=True, null=True)

class PurchaseItemsDelivery(models.Model):
	purchase_items = models.ForeignKey(PurchaseItems, on_delete=models.PROTECT)
	delivery_date = models.DateField()
	delivered_quantity = models.PositiveSmallIntegerField()
	memo = models.TextField(blank=True, null=True)

post_save.connect(add_spareparts_logs, sender=Purchase)
pre_delete.connect(delete_spareparts_logs, sender=Purchase)

post_save.connect(add_spareparts_logs, sender=PurchaseItems)
pre_delete.connect(delete_spareparts_logs, sender=PurchaseItems)