from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Stori, Stori_category, Account, Stori_comment, Comment_reaction, Stori_reaction, Reaction_choice

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

""" Stori admin """
class StoriAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created')
    list_filter = ("status",)
    search_fields = ['title', 'stori']
    prepopulated_fields = {'slug': ('title',)} 

# mixins?
admin.site.register(Account)
admin.site.register(Stori,StoriAdmin)
admin.site.register(Stori_category)
admin.site.register(Stori_comment)
admin.site.register(Comment_reaction)
admin.site.register(Stori_reaction)
admin.site.register(Reaction_choice)
