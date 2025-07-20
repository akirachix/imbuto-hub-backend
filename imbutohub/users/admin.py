from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'gender', 'member_id', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'gender', 'member_id', 'national_id', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'gender')}),
    )
admin.site.register(User, CustomUserAdmin)

















