from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from django.forms.models import inlineformset_factory
from spareparts.purchase.models import Purchase, PurchaseItems, PurchaseItemsDelivery
from spareparts.master.models import MasterSpareParts
from spareparts.purchase.forms import PurchaseForm, PurchaseItemsForm, \
	PurchaseItemsDeliveryForm, PurchaseItemsFormSet
from accounts.models import Origin
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def request_list(request):
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
	return render (request, 'purchase/requestlist.html', context)


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
				return HttpResponseRedirect (reverse('spareparts_purchase:request_list'))
			else:
				return HttpResponse ("save failed items level")
		else:
			return HttpResponse ("save failed in purchase level")

	# to display the form purchase
	form = PurchaseForm()
	formset = PurchaseItemsFormSet()
	master_spare_parts = MasterSpareParts.objects.all()


	context = {
		'form': form,
		'formset': formset,
		'masters': master_spare_parts,
		}

	return render (request, 'purchase/requestadd.html', context)

@login_required(login_url='/login/')
def request_details(request, request_id):

	purchase = Purchase.objects.get(pk=request_id)
	purchase_items = PurchaseItems.objects.filter(purchase=request_id)

	context = {
		'purchase': purchase,
		'items': purchase_items,
		}

	return render (request, 'purchase/requestdetails.html', context)

@login_required(login_url="/login/")
def request_review(request, request_id):
	# to process the update (approval decision)
	if request.method == "POST":
		purchase = Purchase.objects.get(id=request_id)
		if '_approve' in request.POST:
			# code if approved
			purchase.request_approval = True
			purchase.save()
			return HttpResponseRedirect(reverse('sppurchase:request_list'))

		elif '_reject' in request.POST:
			# code if rejected
			purchase.request_reject = True
			purchase.save()
			return HttpResponseRedirect(reverse('sppurchase:request_list'))


	# to display the form
	purchase = Purchase.objects.get(id=request_id)
	purchase_items = PurchaseItems.objects.filter(purchase_id=request_id)

	context = {
		'purchase': purchase,
		'items': purchase_items,
		}

	return render (request, 'purchase/requestreview.html', context)

@login_required(login_url="/login/")
def request_reviewed_list(request):
	purchases = Purchase.objects.filter(request_approval=True)
	context = {
		'purchases': purchases,
		}
	return render (request, 'purchase/requestreviewedlist.html', context)