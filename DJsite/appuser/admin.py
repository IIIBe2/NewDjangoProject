from django.contrib import admin
from .models import UserCustomPermission

@admin.register(UserCustomPermission)
class UserCustomPermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'OpenProduct']
    list_filter = ['OpenProduct']
