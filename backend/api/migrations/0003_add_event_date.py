"""Auto migration to add event_date to Event model."""
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="event_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
