from django.conf.urls import patterns, url
from sppurchase import views

urlpatterns = patterns('',

	url(r'^open/$', views.request_open, name='request_open'),
	url(r'^add/$', views.request_add, name='request_add'),
	url(r'^details/(?P<request_id>\d+)', views.request_details, 
		name='request_details'),
	url(r'^requestapproval/(?P<request_id>\d+)', views.request_approval, 
		name='request_approval'),

	)