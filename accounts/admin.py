from django.contrib import admin
from .models import User
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'mobile',
                    'first_name', 'last_name', 'is_active', ]
    ordering = ['email']
    search_fields = ['mobile', 'email']
    readonly_fields = ['date_joined', 'last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (None, {
            "fields": (
                'email',
                'mobile',
                'password',
            ),
        }),
        (_('Personal info'), {
            "fields": ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            "fields": ('is_staff', 'is_active', 'is_superuser',)
        }),
        (_('Important dates'), {
            "fields": ('last_login', 'date_joined')
        }),
    )

