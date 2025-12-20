from rest_framework import serializers
from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'body', 'active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
