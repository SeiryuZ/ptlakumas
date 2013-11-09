from django.db import models
from basicinfo.models import MachineType, Factory

# Create your models here.
class SparePartsTypes(models.Model):
	spareparts_type = models.CharField(max_length=20)

	class Meta:
		verbose_name = " ref: Spare Part Type"

class MasterSpareParts(models.Model):
	internal_code = models.CharField(max_length=8)
	supplier_code = models.CharField(max_length=20)
	barcode = models.CharField(max_length=100, null=True, blank=True)
	machine_type = models.ForeignKey(MachineType, on_delete=models.PROTECT)

	CHARACTER_CHOICES = (
		('M', 'Mechanical'),
		('E', 'Electrical'),
		)
	character = models.CharField(max_length=1, choices=CHARACTER_CHOICES)

	MOVABILITY_CHOICES = (
		('B', 'Barang bergerak'),
		('N', 'Barang tidak bergerak'),
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

class StockSpareParts(models.Model):
	factory = models.ForeignKey(Factory)
	master_spare_parts = models.ForeignKey(MasterSpareParts)
	initial_quantity = models.PositiveSmallIntegerField()
	quantity = models.PositiveSmallIntegerField()

	class Meta:
		verbose_name = 'Stock'
