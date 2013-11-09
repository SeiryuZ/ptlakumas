from django.contrib import admin
from basicinfo.models import Basic, Factory, Department, MachineType, MachineID

admin.site.register(Basic)
admin.site.register(Factory)
admin.site.register(Department)
admin.site.register(MachineType)
admin.site.register(MachineID)