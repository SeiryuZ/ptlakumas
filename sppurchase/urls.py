from django.conf.urls import patterns, url
from sppurchase import views

urlpatterns = patterns('',

	url(r'^requestlist/$', views.request_list, name='request_list'),
	url(r'^requestadd/$', views.request_add, name='request_add'),
	url(r'^requestdetails/(?P<request_id>\d+)', views.request_details, 
		name='request_details'),
	url(r'^requestreview/(?P<request_id>\d+)', views.request_review, 
		name='request_review'),
	url(r'^requestreviewedlist/$', views.request_reviewed_list, 
		name='request_reviewed_list')

	)