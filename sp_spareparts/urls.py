from django.conf.urls import patterns, url
from sp_spareparts import views

urlpatterns = patterns('',
	url(r'^$', views.default, name='default'),


	)