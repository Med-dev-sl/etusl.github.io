from django.contrib import admin
from .models import Announcement, Event, AboutUniversity, Faculty, News, StrategicPlan, StrategicPlanSection


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created_at')
    list_filter = ('active',)
    search_fields = ('title', 'body')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'event_date', 'created_at')
    search_fields = ('name', 'description', 'location')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AboutUniversity)
class AboutUniversityAdmin(admin.ModelAdmin):
    list_display = ('heading', 'created_at')
    search_fields = ('heading', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Content', {'fields': ('heading', 'description', 'image')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Faculty Information', {'fields': ('name', 'description')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'key_heading', 'date', 'created_at')
    search_fields = ('heading', 'description', 'key_heading')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Content', {'fields': ('key_heading', 'heading', 'description', 'image', 'date')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


class StrategicPlanSectionInline(admin.StackedInline):
    model = StrategicPlanSection
    extra = 1
    readonly_fields = ('created_at', 'image_preview')
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="200" height="auto" />'
        return 'No image'
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


@admin.register(StrategicPlan)
class StrategicPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_image_preview', 'created_at')
    search_fields = ('title', 'summary')
    readonly_fields = ('created_at', 'updated_at', 'main_image_preview')
    inlines = [StrategicPlanSectionInline]
    fieldsets = (
        ('Content', {'fields': ('title', 'summary', 'main_image', 'main_image_preview')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    def main_image_preview(self, obj):
        if obj.main_image:
            return f'<img src="{obj.main_image.url}" width="300" height="auto" />'
        return 'No image'
    main_image_preview.allow_tags = True
    main_image_preview.short_description = 'Main Image Preview'