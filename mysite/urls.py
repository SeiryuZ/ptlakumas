from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^spareparts/', include('spareparts.master.urls', namespace='spareparts_master')),
    url(r'^sppurchase/', include('spareparts.purchase.urls', namespace='spareparts_purchase')),
    url(r'^sptransfer/', include('spareparts.transfer.urls', namespace='spareparts_transfer')),

)
