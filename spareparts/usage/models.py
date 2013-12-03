from django.db import models
from spareparts.master.models import StockSpareParts
from basicinfo.models import MachineID
from django.db.models.signals import post_save, pre_delete
from logs.signals import add_spareparts_logs, delete_spareparts_logs

# Create your models here.

class Adjustment(models.Model):
	stock_spare_parts = models.ForeignKey(StockSpareParts, 
		on_delete=models.PROTECT)
	quantity = models.SmallIntegerField()
	reason = models.CharField(max_length=200, blank=True, null=True)
	memo = models.TextField(blank=True, null=True)

class Replacement(models.Model):
	stock_spare_parts = models.ForeignKey(StockSpareParts,
		on_delete=models.PROTECT)
	machine_id = models.ForeignKey(MachineID) 
	quantity = models.PositiveSmallIntegerField()
	memo = models.TextField(blank=True, null=True)

post_save.connect(add_spareparts_logs, sender=Adjustment)
pre_delete.connect(delete_spareparts_logs, sender=Adjustment)

post_save.connect(add_spareparts_logs, sender=Replacement)
pre_delete.connect(delete_spareparts_logs, sender=Replacement)