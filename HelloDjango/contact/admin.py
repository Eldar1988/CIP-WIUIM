from django.contrib import admin
from .models import Contact, Bot


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date')
    search_fields = ('name', 'phone', 'email', 'date')
    readonly_fields = ('name', 'phone', 'email', 'date')


@admin.register(Bot)
class ContactBot(admin.ModelAdmin):
    list_display = ('number', 'target', 'name', 'create_date')
    search_fields = ('target', 'name')
    list_editable = ('target', 'name')
    readonly_fields = ('create_date',)
