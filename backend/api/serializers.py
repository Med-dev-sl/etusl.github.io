from rest_framework import serializers
from .models import (
    Announcement,
    Event,
    AboutUniversity,
    Faculty,
    News,
    StrategicPlan,
    StrategicPlanSection,
    FooterSection,
    FooterLink,
    AboutSection,
    AboutOverview,
    AboutImage,
    Campus,
    Statistic,
    AboutHistory,
    HistoryEvent,
    HistoryImage,
    VisionMission,
    CoreValue,
    StrategicPriority,
    PriorityItem,
    Affiliate,
    PolicyDocument,
    LeaderPosition,
    Leader,
    AcademicStatistic,
    AdmissionType,
    AcademicPage,
)


class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliate
        fields = ['id', 'name', 'short_description', 'description', 'website', 'contact_email', 'contact_phone', 'address', 'featured_image', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class PolicyDocumentSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = PolicyDocument
        fields = ['id', 'title', 'short_description', 'file', 'file_url', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url) if request is not None else obj.file.url
        return None


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'body', 'active', 'is_featured', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'location', 'photo', 'event_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class AboutUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUniversity
        fields = ['id', 'heading', 'description', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'key_heading', 'heading', 'description', 'date', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class StrategicPlanSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategicPlanSection
        fields = ['id', 'plan', 'heading', 'subheading', 'section_type', 'content', 'items', 'image', 'order', 'created_at']
        read_only_fields = ['id', 'created_at']


class StrategicPlanSerializer(serializers.ModelSerializer):
    sections = StrategicPlanSectionSerializer(many=True, read_only=True)

    class Meta:
        model = StrategicPlan
        fields = ['id', 'title', 'summary', 'main_image', 'sections', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class FooterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = ['id', 'label', 'slug', 'url', 'order', 'created_at']
        read_only_fields = ['id', 'created_at']


class FooterSectionSerializer(serializers.ModelSerializer):
    links = FooterLinkSerializer(many=True, read_only=True)

    class Meta:
        model = FooterSection
        fields = ['id', 'title', 'links', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = ['id', 'about', 'image', 'caption', 'order']
        read_only_fields = ['id']


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ['id', 'about', 'name', 'description', 'image', 'order']
        read_only_fields = ['id']


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ['id', 'about', 'label', 'value', 'order']
        read_only_fields = ['id']


class AboutOverviewSerializer(serializers.ModelSerializer):
    images = AboutImageSerializer(many=True, read_only=True)
    campuses = CampusSerializer(many=True, read_only=True)
    stat_items = StatisticSerializer(many=True, read_only=True)

    class Meta:
        model = AboutOverview
        fields = ['id', 'section', 'brief', 'content', 'statistics', 'images', 'campuses', 'stat_items', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class AboutSectionSerializer(serializers.ModelSerializer):
    overview = AboutOverviewSerializer(read_only=True)

    class Meta:
        model = AboutSection
        fields = ['id', 'title', 'slug', 'order', 'overview', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class HistoryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryEvent
        fields = ['id', 'history', 'year', 'title', 'name', 'description', 'order', 'created_at']
        read_only_fields = ['id', 'created_at']


class HistoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryImage
        fields = ['id', 'history', 'image', 'caption', 'year', 'order', 'created_at']
        read_only_fields = ['id', 'created_at']


class AboutHistorySerializer(serializers.ModelSerializer):
    events = HistoryEventSerializer(many=True, read_only=True)
    images = HistoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = AboutHistory
        fields = ['id', 'title', 'subtitle', 'image', 'content', 'events', 'images', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class PriorityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityItem
        fields = ['id', 'priority', 'text', 'order', 'created_at']
        read_only_fields = ['id', 'created_at']


class StrategicPrioritySerializer(serializers.ModelSerializer):
    items = PriorityItemSerializer(many=True, read_only=True)

    class Meta:
        model = StrategicPriority
        fields = ['id', 'title', 'featured_image', 'image_alt', 'items', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = ['id', 'title', 'description', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class VisionMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisionMission
        fields = ['id', 'vision_title', 'vision_text', 'mission_title', 'mission_text', 'featured_image', 'image_alt', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class LeaderPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderPosition
        fields = ['id', 'title', 'hierarchy_level', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class LeaderSerializer(serializers.ModelSerializer):
    position_title = serializers.CharField(source='position.title', read_only=True)
    position_level = serializers.IntegerField(source='position.hierarchy_level', read_only=True)

    class Meta:
        model = Leader
        fields = ['id', 'user', 'position', 'position_title', 'position_level', 'name', 'photo', 'bio', 'email', 'phone', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class AcademicStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicStatistic
        fields = ['id', 'statistic_type', 'value', 'label', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class AdmissionTypeSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = AdmissionType
        fields = ['id', 'category', 'title', 'description', 'image', 'image_url', 'link_url', 'order', 'active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request is not None else obj.image.url
        return None


class AcademicPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPage
        fields = ['id', 'page_title', 'hero_subtitle', 'overview_title', 'overview_description', 'nurture_title', 'nurture_description', 'study_with_us_link', 'student_handbook_link', 'academic_calendar_link', 'academic_calendar_title', 'academic_calendar_description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']