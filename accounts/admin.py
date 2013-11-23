from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import Origin

class OriginInLine(admin.StackedInline):
	model = Origin

class UserAdmin(UserAdmin):
	inlines = [OriginInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)