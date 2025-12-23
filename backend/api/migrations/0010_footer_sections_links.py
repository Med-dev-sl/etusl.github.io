# Generated migration to add FooterSection and FooterLink models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_announcement_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Footer Section',
                'verbose_name_plural': 'Footer Sections',
                'ordering': ['order', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('order', models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='api.footersection')),
            ],
            options={
                'verbose_name': 'Footer Link',
                'verbose_name_plural': 'Footer Links',
                'ordering': ['order', 'created_at'],
            },
        ),
    ]
