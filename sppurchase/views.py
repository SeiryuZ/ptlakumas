from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.forms.models import inlineformset_factory
from sppurchase.models import Purchase, PurchaseItems, PurchaseItemsDelivery
from sppurchase.forms import PurchaseForm, PurchaseItemsForm, PurchaseItemsDeliveryForm, PurchaseItemsFormSet
from accounts.models import Origin
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def request_open(request):
	user = User.objects.get(pk=request.user.id)
	user_factory = user.origin.factory
	purchases = Purchase.objects.filter(request_approval=False, 
		request_reject=False, factory=user_factory)

	# mungkin harusnya bukan False, tapi 0. Dicoba aja mana yang bener
	# di atas itu namanya filter AND. Kalau filter OR adalah:
		# from django.db.models import Q
		# User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

	context = {
		'purchases': purchases,
	}
	return render (request, 'sppurchase/requestopen.html', context)


@login_required(login_url='/login/')
def request_add(request):
	# to post the addition
	if request.method == "POST":
		form = PurchaseForm(request.POST)
		formset = PurchaseItemsFormSet(request.POST)
		if form.is_valid():
			if formset.is_valid():
				parent_instance = form.save()
				formset.instance = parent_instance
				formset.save()
				return HttpResponseRedirect (reverse('sp_spareparts:spstock'))
			else:
				return HttpResponse ("save failed items level")
		else:
			return HttpResponse ("save failed in purchase level")

	# to display the form purchase
	form = PurchaseForm()
	formset = PurchaseItemsFormSet()


	context = {
		'form': form,
		'formset': formset,
		}

	return render (request, 'sppurchase/requestadd.html', context)

@login_required(login_url='/login/')
def request_details(request, request_id):

	purchase = Purchase.objects.get(pk=request_id)
	purchase_items = PurchaseItems.objects.filter(purchase=request_id)
	form = PurchaseForm(instance=purchase)
	formset = PurchaseItemsFormSet(instance=purchase)

	context = {
		'form': form,
		'formset': formset,
		}

	return render (request, 'sppurchase/requestdetails.html', context)
