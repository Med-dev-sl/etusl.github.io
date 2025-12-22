from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Announcement, Event, AboutUniversity
from .serializers import AnnouncementSerializer, EventSerializer, AboutUniversitySerializer


def status(request):
    """Simple status endpoint for health checks."""
    return JsonResponse({
        'status': 'ok',
        'message': 'Django backend running',
    })


class AnnouncementViewSet(viewsets.ModelViewSet):
    """API endpoint that allows announcements to be viewed or edited."""
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Return only active announcements"""
        qs = self.get_queryset().filter(active=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):
    """API endpoint for events with photo upload."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AboutUniversityViewSet(viewsets.ModelViewSet):
    """API endpoint for about university information."""
    queryset = AboutUniversity.objects.all()
    serializer_class = AboutUniversitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
