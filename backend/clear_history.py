import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_project.settings')
django.setup()

from api.models import HistoryEvent, HistoryImage, AboutHistory

HistoryEvent.objects.all().delete()
HistoryImage.objects.all().delete()
AboutHistory.objects.all().delete()

print("Cleared history tables successfully")
