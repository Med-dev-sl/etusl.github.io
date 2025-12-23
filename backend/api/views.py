from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

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
from .serializers import (
    AnnouncementSerializer,
    EventSerializer,
    AboutUniversitySerializer,
    FacultySerializer,
    NewsSerializer,
    StrategicPlanSerializer,
    StrategicPlanSectionSerializer,
    FooterSectionSerializer,
    FooterLinkSerializer,
    AboutSectionSerializer,
    AboutOverviewSerializer,
    AboutImageSerializer,
    CampusSerializer,
    StatisticSerializer,
)


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


class FooterSectionViewSet(viewsets.ModelViewSet):
    """API endpoint for footer sections with nested links."""
    queryset = FooterSection.objects.all()
    serializer_class = FooterSectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FooterLinkViewSet(viewsets.ModelViewSet):
    """API endpoint for footer links — allows admin to manage links directly if needed."""
    queryset = FooterLink.objects.all()
    serializer_class = FooterLinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AboutSectionViewSet(viewsets.ModelViewSet):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AboutOverviewViewSet(viewsets.ModelViewSet):
    queryset = AboutOverview.objects.all()
    serializer_class = AboutOverviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AboutImageViewSet(viewsets.ModelViewSet):
    queryset = AboutImage.objects.all()
    serializer_class = AboutImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]