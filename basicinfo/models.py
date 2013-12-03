from django.db import models
from django.db.models.signals import post_save, pre_delete
from logs.signals import add_basic_info_logs, delete_basic_info_logs

# Create your models here.
class Basic(models.Model):
	company_name = models.CharField (max_length=50, unique=True)
	ho_address = models.CharField ('head office address', max_length=200)
	phone1 = models.CharField (max_length=20, null=True,blank=True)
	phone2 = models.CharField (max_length=20, null=True, blank=True)
	phone3 = models.CharField (max_length=20, null=True, blank=True)
	fax1 = models.CharField (max_length=20, null=True, blank=True)
	fax2 = models.CharField (max_length=20, null=True, blank=True)
	fax3 = models.CharField (max_length=20, null=True, blank=True)
	email1 = models.EmailField(null=True, blank=True)
	email2 = models.EmailField(null=True, blank=True)
	email3 = models.EmailField(null=True, blank=True)

	def __unicode__(self):
		return self.company_name

class Factory(models.Model):
	code_name = models.CharField (max_length=20, unique=True)
	address = models.CharField (max_length=200)
	phone = models.CharField (max_length=20, null=True, blank=True)
	fax = models.CharField (max_length=20, null=True, blank=True)

	def __unicode__(self):
		return self.code_name

	class Meta:
		verbose_name = "Factorie"

class Department(models.Model):
	department_name = models.CharField (max_length=20, unique=True)

	def __unicode__(self):
		return self.department_name

class MachineType(models.Model):
	department = models.ForeignKey(Department, on_delete=models.PROTECT)
	machine_type = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
		return self.machine_type

class MachineID(models.Model):
	machine_type = models.ForeignKey(MachineType, on_delete=models.PROTECT)
	factory = models.ForeignKey(Factory, on_delete=models.PROTECT)
	machine_number = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
		return self.machine_number

	class Meta:
		verbose_name = "Machine"

post_save.connect(add_basic_info_logs, sender=Factory)
pre_delete.connect(delete_basic_info_logs, sender=Factory)

post_save.connect(add_basic_info_logs, sender=Basic)
pre_delete.connect(delete_basic_info_logs, sender=Basic)

post_save.connect(add_basic_info_logs, sender=Department)
pre_delete.connect(add_basic_info_logs, sender=Department)

post_save.connect(add_basic_info_logs, sender=MachineType)
pre_delete.connect(add_basic_info_logs, sender=MachineType)

post_save.connect(add_basic_info_logs, sender=MachineID)
pre_delete.connect(add_basic_info_logs, sender=MachineID)
