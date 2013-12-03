from django import forms
from django.forms import ModelForm
from spareparts.master.models import SparePartsTypes, MasterSpareParts, \
StockSpareParts

class SparePartsTypesForm(forms.ModelForm):
	class Meta:
		model = SparePartsTypes

class MasterSparePartsForm(forms.ModelForm):
	class Meta:
		model = MasterSpareParts

class StockSparePartsForm(forms.ModelForm):
	class Meta:
		model = StockSpareParts
