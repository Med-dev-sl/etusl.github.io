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
)


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
        fields = ['id', 'plan', 'heading', 'content', 'image', 'order', 'created_at']
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