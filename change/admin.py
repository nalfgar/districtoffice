from django.contrib import admin

from .models import Change, DocumentType, Community


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    empty_value_display = '------'


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    empty_value_display = '------'


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    empty_value_display = '------'
