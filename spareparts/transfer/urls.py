from django.conf.urls import patterns, url
from spareparts.transfer import views

urlpatterns = patterns('',

	url(r'^sptransfer/$', views.spareparts_transfer, name='sptransfer'),
	url(r'^sptransfer/add/$', views.sptransfer_add, name='addrequest'),

	)