from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Announcement, Event, AboutUniversity, Faculty, News, StrategicPlan, StrategicPlanSection
from .serializers import AnnouncementSerializer, EventSerializer, AboutUniversitySerializer, FacultySerializer, NewsSerializer, StrategicPlanSerializer, StrategicPlanSectionSerializer


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

class FacultyViewSet(viewsets.ModelViewSet):
    """API endpoint for faculties."""
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class NewsViewSet(viewsets.ModelViewSet):
    """API endpoint for News items."""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StrategicPlanViewSet(viewsets.ModelViewSet):
    """API endpoint for Strategic Plans. Sections are nested read-only via serializer."""
    queryset = StrategicPlan.objects.all()
    serializer_class = StrategicPlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StrategicPlanSectionViewSet(viewsets.ModelViewSet):
    """API endpoint for sections — allows admin to create/edit sections directly if needed."""
    queryset = StrategicPlanSection.objects.all()
    serializer_class = StrategicPlanSectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]