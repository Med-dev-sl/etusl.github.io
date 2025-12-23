from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_aboutoverview_aboutsection_statistic_campus_and_more'),
        ('api', '0013_seed_about_overview'),
    ]

    operations = [
        # This is an empty merge migration created to unify two conflicting 0013 migrations.
    ]
