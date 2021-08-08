from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()


class UserAdmin(UserAdmin):
    fieldsets = (
        ('System credentials', {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('role', )}),

    )
admin.site.register(User, UserAdmin)