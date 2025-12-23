from rest_framework import serializers
from .models import Announcement, Event, AboutUniversity, Faculty, News, StrategicPlan, StrategicPlanSection


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'body', 'active', 'created_at', 'updated_at']
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