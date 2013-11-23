from django.contrib import admin
from logs.models import SparepartsLog, BasicInfoLog

class SparepartsLogAdmin(admin.ModelAdmin):
	list_display = ('table_name', 'action_type', 'record_id', 
		'modified_by', 'modified_time')

class BasicInfoLogAdmin(admin.ModelAdmin):
	list_display = ('table_name', 'action_type', 'record_id', 
		'modified_by', 'modified_time')


admin.site.register (SparepartsLog, SparepartsLogAdmin)
admin.site.register (BasicInfoLog, BasicInfoLogAdmin)