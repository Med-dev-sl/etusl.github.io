from django.contrib import admin
from .models import (
    Announcement, Event, AboutUniversity, Faculty, News, StrategicPlan, StrategicPlanSection,
    FooterSection, FooterLink, AboutSection, AboutOverview, AboutImage, Campus, Statistic,
    AboutHistory, HistoryEvent, HistoryImage, VisionMission, CoreValue, StrategicPriority, PriorityItem,
    Affiliate, PolicyDocument, LeaderPosition, Leader, AcademicStatistic, AdmissionType, AcademicPage
)


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


class HistoryEventInline(admin.TabularInline):
    model = HistoryEvent
    extra = 1
    fields = ('year', 'title', 'name', 'description', 'order')
    ordering = ('order',)


class HistoryImageInline(admin.TabularInline):
    model = HistoryImage
    extra = 1
    fields = ('image', 'caption', 'year', 'order')
    ordering = ('order',)


@admin.register(AboutHistory)
class AboutHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle', 'content')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    inlines = [HistoryEventInline, HistoryImageInline]
    fieldsets = (
        ('Content', {'fields': ('title', 'subtitle', 'image', 'image_preview', 'content')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="200" height="auto" />'
        return 'No image'
    image_preview.allow_tags = True
    image_preview.short_description = 'Featured Image Preview'


@admin.register(HistoryEvent)
class HistoryEventAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'history', 'order', 'created_at')
    list_filter = ('history',)
    search_fields = ('year', 'title', 'name', 'description')
    readonly_fields = ('created_at',)
    ordering = ('order', '-year')


@admin.register(HistoryImage)
class HistoryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'year', 'history', 'order', 'created_at')
    list_filter = ('history',)
    search_fields = ('caption', 'year')
    readonly_fields = ('created_at', 'image_preview')
    ordering = ('order',)
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" height="auto" />'
        return 'No image'
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


class PriorityItemInline(admin.TabularInline):
    model = PriorityItem
    extra = 1
    fields = ('text', 'order')
    ordering = ('order',)


@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    fieldsets = (
        ('Vision', {'fields': ('vision_title', 'vision_text')}),
        ('Mission', {'fields': ('mission_title', 'mission_text')}),
        ('Featured Image', {'fields': ('featured_image', 'image_alt', 'image_preview')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    def image_preview(self, obj):
        if obj.featured_image:
            return f'<img src="{obj.featured_image.url}" width="200" height="auto" />'
        return 'No image'
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('order',)
    fieldsets = (
        ('Value', {'fields': ('title', 'description', 'order')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(StrategicPriority)
class StrategicPriorityAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    inlines = [PriorityItemInline]
    fieldsets = (
        ('Content', {'fields': ('title', 'featured_image', 'image_alt', 'image_preview')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    def image_preview(self, obj):
        if obj.featured_image:
            return f'<img src="{obj.featured_image.url}" width="200" height="auto" />'
        return 'No image'
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


@admin.register(LeaderPosition)
class LeaderPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'hierarchy_level', 'order', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('hierarchy_level', 'order')
    fieldsets = (
        ('Position Details', {'fields': ('title', 'hierarchy_level', 'order')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order', 'photo_preview', 'user', 'created_at')
    list_filter = ('position__hierarchy_level', 'position')
    search_fields = ('name', 'bio', 'email')
    readonly_fields = ('created_at', 'updated_at', 'photo_preview')
    ordering = ('position__hierarchy_level', 'order')
    fieldsets = (
        ('Personal Information', {'fields': ('name', 'photo', 'photo_preview')}),
        ('Position', {'fields': ('position', 'user')}),
        ('Biography & Contact', {'fields': ('bio', 'email', 'phone')}),
        ('Display', {'fields': ('order',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="100" height="auto" />'
        return 'No photo'
    photo_preview.allow_tags = True
    photo_preview.short_description = 'Photo Preview'

    def get_queryset(self, request):
        """Allow leaders to see/edit only their own profile, admins see all."""
        qs = super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            # Staff but not superuser: only see their own profile
            return qs.filter(user=request.user)
        return qs


@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'created_at')
    search_fields = ('name', 'short_description', 'description')
    readonly_fields = ('created_at', 'updated_at', 'featured_preview')
    fieldsets = (
        ('Content', {'fields': ('name', 'short_description', 'description', 'featured_image', 'featured_preview')}),
        ('Contact', {'fields': ('website', 'contact_email', 'contact_phone', 'address', 'order')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )

    def featured_preview(self, obj):
        if obj.featured_image:
            return f'<img src="{obj.featured_image.url}" width="200" height="auto" />'
        return 'No image'
    featured_preview.allow_tags = True
    featured_preview.short_description = 'Image Preview'

@admin.register(PolicyDocument)
class PolicyDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "file_name", "created_at")
    search_fields = ("title", "short_description")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("order", "title")
    fieldsets = (
        ("Content", {"fields": ("title", "short_description", "file")}),
        ("Display", {"fields": ("order",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    def file_name(self, obj):
        if obj.file:
            return obj.file.name.split("/")[-1]
        return "No file"
    file_name.short_description = "File"


@admin.register(AcademicStatistic)
class AcademicStatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'statistic_type', 'order')
    list_filter = ('statistic_type',)
    ordering = ('order',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Content', {'fields': ('statistic_type', 'value', 'label', 'order')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(AdmissionType)
class AdmissionTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'active', 'order')
    list_filter = ('category', 'active')
    search_fields = ('title', 'description')
    ordering = ('order',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Content', {'fields': ('category', 'title', 'description', 'image', 'link_url')}),
        ('Settings', {'fields': ('active', 'order')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(AcademicPage)
class AcademicPageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Page Titles', {'fields': ('page_title', 'overview_title', 'nurture_title', 'academic_calendar_title')}),
        ('Hero Section', {'fields': ('hero_subtitle',)}),
        ('Overview Section', {'fields': ('overview_description',)}),
        ('Nurture Section', {'fields': ('nurture_description',)}),
        ('Academic Calendar', {'fields': ('academic_calendar_description',)}),
        ('Links', {'fields': ('study_with_us_link', 'student_handbook_link', 'academic_calendar_link')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
