from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'announcements', views.AnnouncementViewSet, basename='announcement')
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'aboutuniversity', views.AboutUniversityViewSet, basename='aboutuniversity')
router.register(r'faculties', views.FacultyViewSet, basename='faculty')

urlpatterns = [
    path('status/', views.status, name='status'),
    path('', include(router.urls)),
]
