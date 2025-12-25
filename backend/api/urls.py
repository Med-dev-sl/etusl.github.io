from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'announcements', views.AnnouncementViewSet, basename='announcement')
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'aboutuniversity', views.AboutUniversityViewSet, basename='aboutuniversity')
router.register(r'faculties', views.FacultyViewSet, basename='faculty')
router.register(r'news', views.NewsViewSet, basename='news')
router.register(r'strategic-plans', views.StrategicPlanViewSet, basename='strategicplan')
router.register(r'strategic-plan-sections', views.StrategicPlanSectionViewSet, basename='strategicplansection')
router.register(r'footer-sections', views.FooterSectionViewSet, basename='footersection')
router.register(r'footer-links', views.FooterLinkViewSet, basename='footerlink')
router.register(r'about-sections', views.AboutSectionViewSet, basename='aboutsection')
router.register(r'about-overviews', views.AboutOverviewViewSet, basename='aboutoverview')
router.register(r'about-images', views.AboutImageViewSet, basename='aboutimage')
router.register(r'about-campuses', views.CampusViewSet, basename='aboutcampus')
router.register(r'about-statistics', views.StatisticViewSet, basename='aboutstatistic')
router.register(r'about-history', views.AboutHistoryViewSet, basename='abouthistory')
router.register(r'history-events', views.HistoryEventViewSet, basename='historyevent')
router.register(r'history-images', views.HistoryImageViewSet, basename='historyimage')
router.register(r'vision-mission', views.VisionMissionViewSet, basename='visionmission')
router.register(r'core-values', views.CoreValueViewSet, basename='corevalue')
router.register(r'strategic-priorities', views.StrategicPriorityViewSet, basename='strategicpriority')
router.register(r'priority-items', views.PriorityItemViewSet, basename='priorityitem')
router.register(r'leader-positions', views.LeaderPositionViewSet, basename='leaderposition')
router.register(r'leaders', views.LeaderViewSet, basename='leader')
router.register(r'affiliates', views.AffiliateViewSet, basename='affiliate')
router.register(r'policies', views.PolicyDocumentViewSet, basename='policydocument')
router.register(r'academic-statistics', views.AcademicStatisticViewSet, basename='academicstatistic')
router.register(r'admission-types', views.AdmissionTypeViewSet, basename='admissiontype')
router.register(r'academic-pages', views.AcademicPageViewSet, basename='academicpage')

urlpatterns = [
    path('status/', views.status, name='status'),
    path('', include(router.urls)),
]
