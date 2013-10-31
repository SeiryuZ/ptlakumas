from django.db import models
from sp_spareparts.models import StockSpareParts
from basicinfo.models import MachineID

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
