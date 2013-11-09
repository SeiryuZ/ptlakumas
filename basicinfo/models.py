from django.db import models

# Create your models here.
class Basic(models.Model):
	company_name = models.CharField (max_length=50)
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

class Factory(models.Model):
	code_name = models.CharField (max_length=20)
	address = models.CharField (max_length=200)
	phone = models.CharField (max_length=20, null=True, blank=True)
	fax = models.CharField (max_length=20, null=True, blank=True)

class Department(models.Model):
	department_name = models.CharField (max_length=20)

class Machine(models.Model):
	machine_type = models.CharField(max_length=20)

class MachineID(models.Model):
	department = models.ForeignKey(Department, on_delete=models.PROTECT)
	