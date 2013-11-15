from logs.models import BasicInfoLog, SparepartsLog
from django.utils import timezone
from django.contrib.auth.models import User
from request_provider.signals import get_request

# create logs for basic info app
def add_basic_info_logs(sender, instance, created, **kwargs):
	request = get_request()
	table_name_logs = '%s' % sender

	if created:
		action_type_logs = 'insert'
	else:
		action_type_logs = 'update'

	record_id_logs = instance.id
	modified_by_logs = request.user
	modified_time_logs = timezone.now()

	log_add = BasicInfoLog(table_name=table_name_logs, 
		action_type=action_type_logs, record_id=record_id_logs, 
		modified_by=modified_by_logs, 
		modified_time=modified_time_logs)
	log_add.save()
	pass

def delete_basic_info_logs(sender, instance, **kwargs):
	request = get_request()
	table_name_logs = '%s' % sender
	action_type_logs = 'delete'
	record_id_logs = instance.id
	modified_by_logs = request.user
	modified_time_logs = timezone.now()

	log_add = BasicInfoLog(table_name=table_name_logs, 
		action_type=action_type_logs, record_id=record_id_logs, 
		modified_by=modified_by_logs, 
		modified_time=modified_time_logs)
	log_add.save()
	pass


# create logs for spareparts app
def add_spareparts_logs(sender, instance, created, **kwargs):
	request = get_request()
	table_name_logs = '%s' % sender

	if created:
		action_type_logs = 'insert'
	else:
		action_type_logs = 'update'

	record_id_logs = instance.id
	modified_by_logs = request.user
	modified_time_logs = timezone.now()

	log_add = SparepartsLog(table_name=table_name_logs, 
		action_type=action_type_logs, record_id=record_id_logs, 
		modified_by=modified_by_logs, 
		modified_time=modified_time_logs)
	log_add.save()
	pass

def delete_spareparts_logs(sender, instance, **kwargs):
	request = get_request()
	table_name_logs = '%s' % sender
	action_type_logs = 'delete'
	record_id_logs = instance.id
	modified_by_logs = request.user
	modified_time_logs = timezone.now()

	log_add = SparepartsLog(table_name=table_name_logs, 
		action_type=action_type_logs, record_id=record_id_logs, 
		modified_by=modified_by_logs, 
		modified_time=modified_time_logs)
	log_add.save()
	pass