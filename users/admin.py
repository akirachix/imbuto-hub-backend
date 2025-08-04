from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('member_id', 'user_type', 'is_superuser', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'user_type')
    search_fields = ('member_id', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('member_id', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'user_type')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member_id', 'password', 'first_name', 'last_name'),
        }),
    )
    ordering = ('member_id',)

admin.site.register(User, UserAdmin)
