# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login as auth_login,\
	logout as auth_logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.signals import request_finished

def login(request):
	return render (request, 'accounts/login.html')

def loginauth(request):
	if request.POST:
		# the 'username' inside POST bracket takes the NAME in the
		# input tag at the html page
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate (username=username, password=password)

		if user is not None:
			if user.is_active:
				auth_login(request,user)
				return HttpResponseRedirect(reverse('spareparts_master:default'))
			else:
				return HttpResponse("Account has been disabled. "\
					"Please contact administrator.")
		else:
			return render (request, 'accounts/loginfailed.html')

def logout(request):
	auth_logout(request)
	return HttpResponse("you are logged out, "\
		"have a nice day and thank you.")
	
