"""Generated migration to add is_featured to Announcement"""
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_announcement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
