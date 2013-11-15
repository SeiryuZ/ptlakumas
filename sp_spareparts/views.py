from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sp_spareparts.models import SparePartsTypes
from sp_spareparts.forms import SparePartsTypesForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models.deletion import ProtectedError

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
