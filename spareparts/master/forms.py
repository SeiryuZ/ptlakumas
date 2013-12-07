from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from spareparts.master.models import SparePartsTypes, MasterSpareParts, \
		StockSpareParts, MachineSuitability

class SparePartsTypesForm(forms.ModelForm):
	class Meta:
		model = SparePartsTypes

class MasterSparePartsForm(forms.ModelForm):
	class Meta:
		model = MasterSpareParts

class StockSparePartsForm(forms.ModelForm):
	class Meta:
		model = StockSpareParts

class MachineSuitabilityForm(forms.ModelForm):
	class Meta:
		model = MachineSuitability

MachineSuitabilityFormSet = inlineformset_factory(MasterSpareParts, MachineSuitability)