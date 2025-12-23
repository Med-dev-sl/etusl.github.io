from django.contrib import admin
from .models import Announcement, Event, AboutUniversity, Faculty, News, StrategicPlan, StrategicPlanSection, FooterSection, FooterLink
from .models import AboutSection, AboutOverview, AboutImage, Campus, Statistic


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'is_featured', 'date', 'created_at')
    list_filter = ('active', 'is_featured')
    search_fields = ('title', 'body')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Content', {'fields': ('title', 'body', 'date', 'active', 'is_featured')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


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


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1
    fields = ('label', 'slug', 'url', 'order')
    ordering = ('order',)


@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [FooterLinkInline]
    fieldsets = (
        ('Content', {'fields': ('title', 'order')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    ordering = ('order',)


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('label', 'section', 'slug', 'order', 'created_at')
    list_filter = ('section',)
    search_fields = ('label', 'url', 'slug')
    readonly_fields = ('created_at',)
    ordering = ('section', 'order')


class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra = 1
    fields = ('image', 'caption', 'order')


class CampusInline(admin.StackedInline):
    model = Campus
    extra = 1
    fields = ('name', 'description', 'image', 'order')


class StatisticInline(admin.TabularInline):
    model = Statistic
    extra = 1
    fields = ('label', 'value', 'order')


@admin.register(AboutOverview)
class AboutOverviewAdmin(admin.ModelAdmin):
    list_display = ('section', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [AboutImageInline, CampusInline, StatisticInline]
    fieldsets = (
        ('Content', {'fields': ('section', 'brief', 'content', 'statistics')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order', 'created_at')
    search_fields = ('title', 'slug')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Section', {'fields': ('title', 'slug', 'order')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )