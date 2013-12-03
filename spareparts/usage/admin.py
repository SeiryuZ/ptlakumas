from django.contrib import admin
from spareparts.usage.models import Adjustment, Replacement

admin.site.register(Adjustment)
admin.site.register(Replacement)