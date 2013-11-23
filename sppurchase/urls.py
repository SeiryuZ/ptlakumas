from django.conf.urls import patterns, url
from sppurchase import views

urlpatterns = patterns('',

	url(r'^sppurchase/open/$', views.request_open, name='request_open'),
	url(r'^sppurchase/add/$', views.request_add, name='request_add'),
	url(r'^sppurchase/details/(?P<request_id>\d+)', views.request_details, 
		name='request_details'),

	)