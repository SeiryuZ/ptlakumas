from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sp_spareparts.models import SparePartsTypes, MasterSpareParts, StockSpareParts
from sp_spareparts.forms import SparePartsTypesForm, MasterSparePartsForm, StockSparePartsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError
import json as simplejson
from django.core import serializers
# to stop execution, put below code whereever you wanna stop
# and then directly from the console you can print (print request.POST, request.GET, request.user)
# without changing the views.
# import pdb; pdb.set_trace()

# Create your views here.

@login_required(login_url='/login/')
def default(request):
	return render(request, 'sp_spareparts/default.html')

@login_required(login_url='/login/')
def spareparts_types(request):
	spareparts_types = SparePartsTypes.objects.all()
	context = {
		'types': spareparts_types,
		}
	return render(request, 'sp_spareparts/sptypes.html', context)

@login_required(login_url='/login/')
def form_add_types(request):
	# to process the addition
	if request.method == 'POST':
		form = SparePartsTypesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('sp_spareparts:sptypes'))
		else:
			return HttpResponse('Some of the data are not entered correctly')

	# to display the form
	form = SparePartsTypesForm()
	context = {
		'form' : form,
		}
	return render(request, 'sp_spareparts/sptypesadd.html', context)

@login_required(login_url='/login/')
def edit_types(request, type_id):
	# to process the update
	if request.method == 'POST':
		spareparts_types = SparePartsTypes.objects.get(pk=type_id)
		form = SparePartsTypesForm(request.POST, instance=spareparts_types)

		if form.is_valid():
			spareparts_types = form.save(commit=False)
			spareparts_types.save()
			return HttpResponseRedirect(reverse('sp_spareparts:sptypes'))
		else:
			return HttpResponse('Some of the data are not entered correctly')


	# to display the edit form for related instance
	spareparts_types = SparePartsTypes.objects.get(pk=type_id)
	form = SparePartsTypesForm(instance=spareparts_types)
	context = {
		'form': form,
		'type': spareparts_types,
		}
	return render(request, 'sp_spareparts/sptypesedit.html', context)

@login_required(login_url='/login/')
def delete_types(request, type_id):
	# to process the deletetion
	try:
		spareparts_types = SparePartsTypes.objects.get(pk=type_id).delete()
	except ProtectedError:
		HttpResponse ("there is child data. cannot delete object")

	return HttpResponseRedirect(reverse('sp_spareparts:sptypes'))

@login_required(login_url='/login/')
def master_spareparts_list(request):
	master_spare_parts = MasterSpareParts.objects.all()
	sort = request.GET['sort']
	if sort == 'supplier_code':
		master_spare_parts = master_spare_parts.order_by('supplier_code')
	context = {
		'master': master_spare_parts,
		}
	return render(request, 'sp_spareparts/spmaster.html', context)

@login_required(login_url='/login/')
def add_master(request):
	# to process the addtion
	if request.method =='POST':
		form = MasterSparePartsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('sp_spareparts:spmaster'))
		else:
			print (request.POST)
			# return HttpResponse("some data are not entered corrently")
	

	# to display the form
	form = MasterSparePartsForm()
	context = {
		'form' : form,
		}
	return render (request, 'sp_spareparts/spmasteradd.html', context)

@login_required(login_url='/login/')
def edit_master(request, master_id):
	# to process the update
	if request.method == 'POST':
		master_spare_parts = MasterSpareParts.objects.get(pk=master_id)
		form = MasterSparePartsForm(request.POST, instance=master_spare_parts)
		if form.is_valid():
			master_spare_parts = form.save(commit=False)
			master_spare_parts.save()
			return HttpResponseRedirect(reverse('sp_spareparts:spmaster'))
		else:
			return HttpResponse ("some data are not entered corrently")

	# to display the form of related object
	master_spare_parts = MasterSpareParts.objects.get(pk=master_id)
	form = MasterSparePartsForm(instance=master_spare_parts)
	context = {
		'form' : form,
		'master' : master_spare_parts,
	}
	return render (request, 'sp_spareparts/spmasteredit.html', context)


@login_required(login_url='/login/')
def delete_master(request,master_id):
	# to process the deletion
	try:
		master_spare_parts = MasterSpareParts.objects.get(pk=master_id).delete()
	except ProtectedError:
		return HttpResponse ("data cannot be deleted, child data is protected")

	return HttpResponseRedirect(reverse('sp_spareparts:spmaster'))

@login_required(login_url='/login/')
def stock_spareparts_list(request):
	stock_spareparts_list = StockSpareParts.objects.all()
	context = {
		'stocks' : stock_spareparts_list
		}
	return render (request, 'sp_spareparts/spstock.html', context)

@login_required(login_url="/login/")
def test_json(request):
	# get the objects
	master_spare_parts = MasterSpareParts.objects.all()

	# make it as dictionary
	data = serializers.serialize ("json", master_spare_parts)

	# convert the list into JSON
	response_data = simplejson.dumps(data)

	# return an HttpResponse with JSON and correct mime type
	return HttpResponse(response_data, mimetype='application/json')



@login_required(login_url="/login/")
def json_result(request):
	return render (request, 'sp_spareparts/jsonresult.html')