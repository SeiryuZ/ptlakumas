from django.conf.urls import patterns, url
from sp_spareparts import views

urlpatterns = patterns('',
	url(r'^$', views.default, name='default'),
	url(r'^sptypes/$', views.spareparts_types, name='sptypes'),
	url(r'^sptypes/add/$', views.form_add_types, name='sptypesadd'),
	url(r'^sptypes/edit/(?P<type_id>\d+)', 
		views.edit_types, name='sptypesedit'),
	url(r'^sptypes/delete/(?P<type_id>\d+)', 
		views.delete_types, name='sptypesdelete'),
	)