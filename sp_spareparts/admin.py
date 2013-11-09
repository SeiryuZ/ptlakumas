from django.contrib import admin
from sp_spareparts.models import SparePartsTypes, MasterSpareParts, StockSpareParts

admin.site.register(SparePartsTypes)
admin.site.register(MasterSpareParts)
admin.site.register(StockSpareParts)
