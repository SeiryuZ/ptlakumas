from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
	url(r'^$', views.login, name='login'),
	url(r'^login/$', views.login, name='login'),
	url(r'^loginauth/$', views.loginauth, name='loginauth'),
	url(r'^logout/$', views.logout, name='logout'),

	)