from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from sppurchase.models import Purchase, PurchaseItems, PurchaseItemsDelivery

class PurchaseForm(forms.ModelForm):
	class Meta:
		model = Purchase

class PurchaseItemsForm(forms.ModelForm):
	class Meta:
		model = PurchaseItems

class PurchaseItemsDeliveryForm(forms.ModelForm):
	class Meta:
		model = PurchaseItemsDelivery

PurchaseItemsFormSet = inlineformset_factory(Purchase, PurchaseItems)