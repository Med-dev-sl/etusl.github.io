# Generated migration to add slug field to FooterLink and make url optional
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_footerlink_id_alter_footersection_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerlink',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='footerlink',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
