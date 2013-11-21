from fabric.api import local, settings, lcd, run

apps_to_watch = ["accounts", "basicinfo", "logs", "sp_spareparts",
				"sppermit", "sppurchase", "sptransfer",
				"spusage"]

def schemamigration_auto():
	with settings(warn_only=True):
		for app in apps_to_watch:
			local ("manage.py schemamigration %s --auto" % app)

def schemamigration_initial():
	with settings(warn_only=True):
		for app in apps_to_watch:
			local ("manage.py schemamigration %s --initial" % app)

def migrate_initial():
	schemamigration_initial()
	local ("manage.py migrate")

def migrate_auto():
	schemamigration_auto()
	local ("manage.py migrate")

def delete_migrations_folders():
	with settings(warn_only=True):
		for app in apps_to_watch:
			with lcd ("/%s" % app):
				local ("rmdir migrations /s")

def test():
	with lcd("/../Users/Win7/Desktop/ptlakumas/webapp"):
		local ("dir")
