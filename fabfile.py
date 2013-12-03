from fabric.api import local, settings, lcd

root_apps_to_watch = ["accounts", "basicinfo", "logs", "spareparts/master",
				"spareparts/permit", "spareparts/purchase", "spareparts/transfer",
				"spareparts/usage"]

spareparts_apps = ["master","permit", "purchase", "transfer", "usage"]



new_apps = []


def schemamigration_initial():
	for app in new_apps:
		local ("manage.py schemamigration %s --initial" % app)

def migrate_initial():
	schemamigration_initial()
	local ("manage.py migrate")

def schemamigration_auto():
	with settings(warn_only=True):
		for app in root_apps_to_watch:
			local ("manage.py schemamigration %s --auto" % app)

def migrate_auto():
	schemamigration_auto()
	local ("manage.py migrate")

def delete_migrations_folders():
	for app in root_apps_to_watch:
		with lcd("/../Users/Win7/Desktop/ptlakumas/webapp/%s" % app):
			local ("rmdir migrations /s /q")

	for app in spareparts_apps:
		with lcd("/../Users/Win7/Desktop/ptlakumas/webapp/spareparts/%s" % app):
			local ("rmdir migrations /s /q")

def initiate_database():
	local ("mysql --host=localhost --user=root --password")

def build_database():
	local ("manage.py syncdb")
	for app in root_apps_to_watch:
		local ("manage.py convert_to_south %s" % app)

	for app in spareparts_apps:
		local ("manage.py convert_to_south %s" % app)

def git_push(version):
	local ("git add -A")
	local ("git commit -m %s" % version)
	local ("git push origin master")

# to rebuild database:
# 1. drop the whole schema from workbench
# 2. run fab delete_migrations_folders
# 3. run fab initiate_database
# 4. run fab build_database

# to push to git
# type fab git_push:0.14