from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile, Company


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_logo', 'user', 'name', 'main_phone', 'mail', 'register_date')
    search_fields = ('name', 'mail')
    list_editable = ('name', 'main_phone', 'mail',)
    readonly_fields = ('get_logo',)

    def get_logo(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="75"')

    get_logo.short_description = 'Аватар'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'main_phone', 'mail', 'get_logo', 'register_date')
    list_editable = ('user', 'main_phone', 'mail')
    search_fields = ('name',)
    list_filter = ('user',)
    readonly_fields = ('get_logo',)

    def get_logo(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" width="100"')

    get_logo.short_description = 'Логотип'


