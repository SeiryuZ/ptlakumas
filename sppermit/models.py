from django.db import models

# Create your models here.
class Permit(models.Model):
	number = models.CharField(max_length=20, unique=True)
	car_license = models.CharField(max_length=10)
	car_type = models.CharField(max_length = 20)
	car_brand = models.CharField(max_length=20)
	driver = models.CharField(max_length=20)
	date_go = models.DateField()

	def __unicode__(self):
		return self.number

class PermitItems(models.Model):
	permit_number = models.ForeignKey(Permit)
	item = models.CharField(max_length=100)
	quantity = models.PositiveSmallIntegerField()