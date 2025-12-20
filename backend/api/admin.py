from django.contrib import admin
from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created_at')
    list_filter = ('active',)
    search_fields = ('title', 'body')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
