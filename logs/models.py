from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SparepartsLog(models.Model):
	table_name = models.CharField(max_length=100)
	action_type = models.CharField(max_length=100)
	record_id = models.CharField(max_length=100)
	modified_by = models.CharField(max_length=100)
	modified_time = models.DateTimeField()

	class Meta:
		verbose_name = "Spareparts Log"

class BasicInfoLog(models.Model):
	table_name = models.CharField(max_length=100)
	action_type = models.CharField(max_length=100)
	record_id = models.CharField(max_length=100)
	modified_by = models.CharField(max_length=100)
	modified_time = models.DateTimeField()

	class Meta:
		verbose_name = "Basic Log"
