from django.db import models
from django.contrib.auth.models import User
from basicinfo.models import Factory

# Create your models here.
class Origin(models.Model):
	user = models.OneToOneField(User)
	factory = models.ForeignKey(Factory)
