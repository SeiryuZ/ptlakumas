from django.contrib import admin
from spareparts.master.models import SparePartsTypes, MasterSpareParts, StockSpareParts, MachineSuitability

admin.site.register(SparePartsTypes)
admin.site.register(MasterSpareParts)
admin.site.register(StockSpareParts)
admin.site.register(MachineSuitability)
