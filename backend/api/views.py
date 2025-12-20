from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Announcement
from .serializers import AnnouncementSerializer


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
