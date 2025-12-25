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
    AboutHistorySerializer,
    HistoryEventSerializer,
    HistoryImageSerializer,
    VisionMissionSerializer,
    CoreValueSerializer,
    StrategicPrioritySerializer,
    PriorityItemSerializer,
    AffiliateSerializer,
    PolicyDocumentSerializer,
    LeaderPositionSerializer,
    LeaderSerializer,
    AcademicStatisticSerializer,
    AdmissionTypeSerializer,
    AcademicPageSerializer,
)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to allow leaders to edit only their own profile."""
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff


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


class AboutHistoryViewSet(viewsets.ModelViewSet):
    """API endpoint for university history with events and images."""
    queryset = AboutHistory.objects.all()
    serializer_class = AboutHistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HistoryEventViewSet(viewsets.ModelViewSet):
    """API endpoint for history events/milestones."""
    queryset = HistoryEvent.objects.all()
    serializer_class = HistoryEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HistoryImageViewSet(viewsets.ModelViewSet):
    """API endpoint for history images (gallery)."""
    queryset = HistoryImage.objects.all()
    serializer_class = HistoryImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VisionMissionViewSet(viewsets.ModelViewSet):
    """API endpoint for vision and mission statements."""
    queryset = VisionMission.objects.all()
    serializer_class = VisionMissionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CoreValueViewSet(viewsets.ModelViewSet):
    """API endpoint for core values."""
    queryset = CoreValue.objects.all()
    serializer_class = CoreValueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StrategicPriorityViewSet(viewsets.ModelViewSet):
    """API endpoint for strategic priorities with items."""
    queryset = StrategicPriority.objects.all()
    serializer_class = StrategicPrioritySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PriorityItemViewSet(viewsets.ModelViewSet):
    """API endpoint for priority items."""
    queryset = PriorityItem.objects.all()
    serializer_class = PriorityItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AffiliateViewSet(viewsets.ModelViewSet):
    """API endpoint for affiliated institutions."""
    queryset = Affiliate.objects.all()
    serializer_class = AffiliateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PolicyDocumentViewSet(viewsets.ModelViewSet):
    """API endpoint for policy documents (file upload/download)."""
    queryset = PolicyDocument.objects.all()
    serializer_class = PolicyDocumentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PolicyDocumentViewSet(viewsets.ModelViewSet):
    """API endpoint for policy documents (file upload/download)."""
    queryset = PolicyDocument.objects.all()
    serializer_class = PolicyDocumentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LeaderPositionViewSet(viewsets.ModelViewSet):
    """API endpoint for leader positions."""
    queryset = LeaderPosition.objects.all()
    serializer_class = LeaderPositionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LeaderViewSet(viewsets.ModelViewSet):
    """API endpoint for university leaders with permission control."""
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """Return all leaders (leaders can only edit their own)."""
        return Leader.objects.all()


class AcademicStatisticViewSet(viewsets.ModelViewSet):
    """API endpoint for academic statistics."""
    queryset = AcademicStatistic.objects.all()
    serializer_class = AcademicStatisticSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdmissionTypeViewSet(viewsets.ModelViewSet):
    """API endpoint for admission types."""
    queryset = AdmissionType.objects.filter(active=True)
    serializer_class = AdmissionTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AcademicPageViewSet(viewsets.ModelViewSet):
    """API endpoint for academic page content."""
    queryset = AcademicPage.objects.all()
    serializer_class = AcademicPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def current(self, request):
        """Return the current/first academic page"""
        page = AcademicPage.objects.first()
        if page:
            serializer = self.get_serializer(page)
            return Response(serializer.data)
        return Response({'error': 'No academic page configured'}, status=404)