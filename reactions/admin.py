from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Stori, Stori_category, Account, Stori_comment, Comment_reaction, Stori_reaction

# Register your models here.#
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}),
    )

# mixins?
admin.site.register(Account)
