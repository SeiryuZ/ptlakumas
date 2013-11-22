from fabric.api import local, settings, lcd

apps_to_watch = ["accounts", "basicinfo", "logs", "sp_spareparts",
				"sppermit", "sppurchase", "sptransfer",
				"spusage"]

new_apps = []


def schemamigration_initial():
	for app in new_apps:
		local ("manage.py schemamigration %s --initial" % app)

def migrate_initial():
	schemamigration_initial()
	local ("manage.py migrate")

def schemamigration_auto():
with settings(warn_only=True):
	for app in apps_to_watch:
		local ("manage.py schemamigration %s --auto" % app)

def migrate_auto():
	schemamigration_auto()
	local ("manage.py migrate")

def delete_migrations_folders():
	for app in apps_to_watch:
		with lcd("/../Users/Win7/Desktop/ptlakumas/webapp/%s" % app):
			local ("rmdir migrations /s /q")

def initiate_database():
	local ("mysql --host=localhost --user=root --password")

def build_database():
	local ("manage.py syncdb")
	for app in apps_to_watch:
		local ("manage.py convert_to_south %s" % app)

# to rebuild database:
# 1. drop the whole schema from workbench
# 2. run fab delete_migrations_folders
# 3. run fab initiate_database
# 4. run fab build_database