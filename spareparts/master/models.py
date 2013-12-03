from django.db import models
from basicinfo.models import MachineType, Factory
from django.db.models.signals import post_save, pre_delete
from logs.signals import add_spareparts_logs, delete_spareparts_logs

# Create your models here.
class SparePartsTypes(models.Model):
	spareparts_type = models.CharField(max_length=20, unique=True)

	class Meta:
		verbose_name = " ref: Spareparts Type"

	def  __unicode__(self):
		return self.spareparts_type

class MasterSpareParts(models.Model):
	internal_code = models.CharField(max_length=8, unique=True)
	supplier_code = models.CharField(max_length=20)
	barcode = models.CharField(max_length=100, null=True, blank=True)
	machine_type = models.ForeignKey(MachineType, on_delete=models.PROTECT)

	CHARACTER_CHOICES = (
		('M', 'Mechanical'),
		('E', 'Electrical'),
		)
	character = models.CharField(max_length=1, choices=CHARACTER_CHOICES)

	MOVABILITY_CHOICES = (
		('M', 'Moving'),
		('S', 'Static'),
		)
	movability = models.CharField(max_length=1, choices=MOVABILITY_CHOICES)
	
	chain_wheel_type = models.CharField(max_length=20, null=True, blank=True)
	spareparts_type = models.ForeignKey(SparePartsTypes, 
		on_delete=models.PROTECT)

	NATURAL_FREQUENCY_CHOICES = (
		('H', 'High-moving'),
		('M', 'Moderate-moving'),
		('S', 'Slow-moving')
		)
	natural_frequency = models.CharField(max_length=1, 
		choices=NATURAL_FREQUENCY_CHOICES, null=True, blank=True)

	lifetime = models.PositiveSmallIntegerField(
		'estimated life time (months)', null=True, blank=True)

	class Meta:
		verbose_name = 'Master Data Spare Part'

	def __unicode__(self):
		return self.internal_code + " / " + self.supplier_code

class StockSpareParts(models.Model):
	factory = models.ForeignKey(Factory)
	master_spare_parts = models.ForeignKey(MasterSpareParts)
	initial_quantity = models.PositiveSmallIntegerField()
	quantity = models.PositiveSmallIntegerField()

	class Meta:
		verbose_name = 'Stock'

post_save.connect(add_spareparts_logs, sender=SparePartsTypes)
pre_delete.connect(delete_spareparts_logs, sender=SparePartsTypes)

post_save.connect(add_spareparts_logs, sender=MasterSpareParts)
pre_delete.connect(delete_spareparts_logs, sender=MasterSpareParts)

post_save.connect(add_spareparts_logs, sender=StockSpareParts)
pre_delete.connect(delete_spareparts_logs, sender=StockSpareParts)
