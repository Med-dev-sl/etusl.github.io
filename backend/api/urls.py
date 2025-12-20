from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'announcements', views.AnnouncementViewSet, basename='announcement')

urlpatterns = [
    path('status/', views.status, name='status'),
    path('', include(router.urls)),
]
