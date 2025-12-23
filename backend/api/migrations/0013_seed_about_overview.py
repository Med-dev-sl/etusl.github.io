from django.db import migrations


def create_about_overview(apps, schema_editor):
    AboutSection = apps.get_model('api', 'AboutSection')
    AboutOverview = apps.get_model('api', 'AboutOverview')
    Statistic = apps.get_model('api', 'Statistic')
    Campus = apps.get_model('api', 'Campus')

    # Create or get the Overview section
    section, _ = AboutSection.objects.get_or_create(
        slug='overview',
        defaults={'title': 'Overview', 'order': 0}
    )

    # Create an AboutOverview record attached to the section
    overview, _ = AboutOverview.objects.get_or_create(
        section=section,
        defaults={
            'brief': '<p>Eastern Technical University (ETU) is committed to providing high-quality technical and professional education across multiple campuses.</p>',
            'content': '<p>ETU combines teaching, research and service to the community. This seeded content is for demo purposes and can be edited in the admin.</p>',
            'statistics': {'students_total': 63646, 'international': 667, 'graduates': 9509, 'staff': 6565},
        }
    )

    # Seed structured statistic items (order matters for presentation)
    stats = [
        ('Undergraduate Students', '63,646', 1),
        ('International Students', '667', 2),
        ('Graduate Students', '9,509', 3),
        ('Faculty & Staff', '6,565', 4),
    ]
    for label, value, order in stats:
        Statistic.objects.get_or_create(
            about=overview,
            label=label,
            defaults={'value': value, 'order': order}
        )

    # Seed a couple of campuses (images intentionally left blank for admin upload)
    campuses = [
        ('City Campus', 'The central campus located in the city centre providing core faculties.'),
        ('North Campus', 'Campus with strong engineering and applied sciences programs.'),
    ]
    for idx, (name, desc) in enumerate(campuses, start=1):
        Campus.objects.get_or_create(
            about=overview,
            name=name,
            defaults={'description': desc, 'order': idx}
        )


def remove_about_overview(apps, schema_editor):
    AboutSection = apps.get_model('api', 'AboutSection')
    try:
        section = AboutSection.objects.get(slug='overview')
        section.delete()
    except AboutSection.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_footerlink_slug'),
    ]

    operations = [
        migrations.RunPython(create_about_overview, remove_about_overview),
    ]
