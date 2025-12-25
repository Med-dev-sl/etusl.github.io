from django.db import migrations, models


def create_sample_history(apps, schema_editor):
    HistoryEvent = apps.get_model('api', 'HistoryEvent')
    samples = [
        {
            'year': '1960',
            'title': 'Founding of the College',
            'subtitle': 'A humble beginning',
            'description': 'The college was established with a small cohort of dedicated students and staff.',
            'order': 0,
        },
        {
            'year': '1978',
            'title': 'First Graduation Ceremony',
            'subtitle': 'Milestone achievement',
            'description': 'The institution celebrated its first graduating class, marking a new era.',
            'order': 1,
        },
        {
            'year': '1995',
            'title': 'Campus Expansion',
            'subtitle': 'New faculties and facilities',
            'description': 'Major expansion added new faculties and modern teaching facilities.',
            'order': 2,
        },
        {
            'year': '2010',
            'title': 'Research Recognition',
            'subtitle': 'International partnerships',
            'description': 'The university established several international research partnerships.',
            'order': 3,
        },
        {
            'year': '2022',
            'title': 'Digital Transformation',
            'subtitle': 'Modern services',
            'description': 'A full digital transformation improved access to services for students and staff.',
            'order': 4,
        },
    ]
    for item in samples:
        HistoryEvent.objects.create(**item)


def delete_sample_history(apps, schema_editor):
    HistoryEvent = apps.get_model('api', 'HistoryEvent')
    HistoryEvent.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_merge_0013_conflicts'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/history/%Y/%m/%d/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['order', 'year'], 'verbose_name': 'History Event', 'verbose_name_plural': 'History Events'},
        ),
        migrations.RunPython(create_sample_history, delete_sample_history),
    ]
