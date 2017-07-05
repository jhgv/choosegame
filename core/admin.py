from django.contrib import admin

from core.models import UserPreference, UserHiddenPreference

admin.site.register(UserPreference)
admin.site.register(UserHiddenPreference)
# Register your models here.
