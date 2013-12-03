from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
from spareparts.transfer.models import Transfer, TransferItems, TransferItemsDelivery
# from sptransfer.forms import TransferForm, TransferItemsForm, TransferItemsDeliveryForm

@login_required(login_url='/login/')
def spareparts_transfer(request):
	return HttpResponse("this is the dummy page for request transfer")

@login_required(login_url='/login/')
def sptransfer_add(request):
	return HttpResponse ("this is the dummy page to add request transfer")