"""
Django Custom Admin
"""

from django.contrib import admin
# User admin is the base class for admin so we called it Base User admin for 
# consistencey of base name.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# translate from one lang to another, future proofing?
# translate the value we are putting in
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """ Define admin page for users."""
    ordering = ['id']
    list_display = ['email','name']
    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            (_('Personal Info'), {'fields': ('name',)}),
            (
                _('Permissions'),
                {
                    'fields': (
                        'is_active',
                        'is_staff',
                        'is_superuser',
                    )
                }
            ),
            (_('Important Dates'), {'fields': ('last_login',)}),
        )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

    
admin.site.register(models.User,UserAdmin)