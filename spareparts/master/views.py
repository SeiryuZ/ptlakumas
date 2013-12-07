from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from spareparts.master.models import SparePartsTypes, MasterSpareParts, \
	StockSpareParts, MachineSuitability
from spareparts.master.forms import SparePartsTypesForm, MasterSparePartsForm, \
	StockSparePartsForm, MachineSuitabilityForm, MachineSuitabilityFormSet
from basicinfo.models import MachineType
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
	return render(request, 'master/default.html')

@login_required(login_url='/login/')
def spareparts_types(request):
	spareparts_types = SparePartsTypes.objects.all()
	context = {
		'types': spareparts_types,
		}
	return render(request, 'master/sptypes.html', context)

@login_required(login_url='/login/')
def form_add_types(request):
	# to process the addition
	if request.method == 'POST':
		form = SparePartsTypesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('spareparts_master:sptypes'))
		else:
			return HttpResponse('Some of the data are not entered correctly')

	# to display the form
	form = SparePartsTypesForm()
	context = {
		'form' : form,
		}
	return render(request, 'master/sptypesadd.html', context)

@login_required(login_url='/login/')
def edit_types(request, type_id):
	# to process the update
	if request.method == 'POST':
		spareparts_types = SparePartsTypes.objects.get(pk=type_id)
		form = SparePartsTypesForm(request.POST, instance=spareparts_types)

		if form.is_valid():
			spareparts_types = form.save(commit=False)
			spareparts_types.save()
			return HttpResponseRedirect(reverse('spareparts_master:sptypes'))
		else:
			return HttpResponse('Some of the data are not entered correctly')


	# to display the edit form for related instance
	spareparts_types = SparePartsTypes.objects.get(pk=type_id)
	form = SparePartsTypesForm(instance=spareparts_types)
	context = {
		'form': form,
		'type': spareparts_types,
		}
	return render(request, 'master/sptypesedit.html', context)

@login_required(login_url='/login/')
def delete_types(request, type_id):
	# to process the deletetion
	try:
		spareparts_types = SparePartsTypes.objects.get(pk=type_id).delete()
	except ProtectedError:
		return HttpResponse ("there is child data. cannot delete object")

	return HttpResponseRedirect(reverse('spareparts_master:sptypes'))

@login_required(login_url='/login/')
def master_spareparts_list(request):
	master_spare_parts = MasterSpareParts.objects.all()
	sort = request.GET.get('sort')
	if sort == 'supplier_code':
		master_spare_parts = master_spare_parts.order_by('supplier_code')
	elif sort == 'rev_supplier_code':
		master_spare_parts = master_spare_parts.order_by('-supplier_code')

	
	context = {
		'master': master_spare_parts,
		}
	return render(request, 'master/spmaster.html', context)

@login_required(login_url='/login/')
def add_master(request):
	# to process the addtion
	if request.method =='POST':
		form = MasterSparePartsForm(request.POST)
		formset = MachineSuitabilityFormSet(request.POST)
		if form.is_valid():
			if formset.is_valid():
				parent_instance = form.save()
				formset.instance = parent_instance
				formset.save()
				return HttpResponseRedirect(reverse('spareparts_master:spmaster'))
			else:
				return HttpResponse ("save failed items level")
		else:
			return HttpResponse("some data are not entered corrently")
	

	# to display the form
	form = MasterSparePartsForm()
	formset = MachineSuitabilityFormSet()
	machine_type = MachineType.objects.all()
	context = {
		'form' : form,
		'formset': formset,
		'types': machine_type,
		}
	return render (request, 'master/spmasteradd.html', context)

@login_required(login_url='/login/')
def edit_master(request, master_id):
	# to process the update
	if request.method == 'POST':
		master_spare_parts = MasterSpareParts.objects.get(pk=master_id)
		form = MasterSparePartsForm(request.POST, instance=master_spare_parts)
		formset = MachineSuitabilityFormSet(request.POST, request.FILES, instance=master_spare_parts)

		if form.is_valid():
			if formset.is_valid():
				master_spare_parts = form.save()
				formset.save()
				print request.POST
				print request.FILES
				return HttpResponseRedirect(reverse('spareparts_master:spmaster'))
			else:
				return HttpResponse ("Formset data is invalid")
		else:
			return HttpResponse ("Form data is invalid")

	# to display the form of related object
	master_spare_parts = MasterSpareParts.objects.get(pk=master_id)
	machine_suitability = MachineSuitability.objects.filter(master_spare_parts_id=master_id)
	form = MasterSparePartsForm(instance=master_spare_parts)
	formset = MachineSuitabilityFormSet(instance=master_spare_parts)

	context = {
		'form' : form,
		'formset': formset,
		'machine_suitability': machine_suitability,
		'master' : master_spare_parts,
	}
	return render (request, 'master/spmasteredit.html', context)


@login_required(login_url='/login/')
def delete_master(request,master_id):
	# to process the deletion
	try:
		master_spare_parts = MasterSpareParts.objects.get(pk=master_id).delete()
	except ProtectedError:
		return HttpResponse ("data cannot be deleted, child data is protected")

	return HttpResponseRedirect(reverse('spareparts_master:spmaster'))

@login_required(login_url='/login/')
def stock_spareparts_list(request):
	stock_spareparts_list = StockSpareParts.objects.all()
	context = {
		'stocks' : stock_spareparts_list
		}
	return render (request, 'master/spstock.html', context)

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
	return render (request, 'master/jsonresult.html')