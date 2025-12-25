from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_abouthistory'),
    ]

    operations = [
        # First remove sample data
        migrations.RunSQL(
            sql='DELETE FROM api_historyevent;',
            reverse_sql='-- No reverse',
        ),
        # Remove old fields from HistoryEvent
        migrations.RemoveField(
            model_name='historyevent',
            name='image',
        ),
        migrations.RemoveField(
            model_name='historyevent',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='historyevent',
            name='updated_at',
        ),
        # Add foreign key to AboutHistory
        migrations.AddField(
            model_name='historyevent',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.abouthistory'),
            preserve_default=False,
        ),
        # Add name field
        migrations.AddField(
            model_name='historyevent',
            name='name',
            field=models.CharField(blank=True, help_text='Alternative field for event name', max_length=255, default=''),
            preserve_default=False,
        ),
        # Update AboutHistory model options
        migrations.AlterModelOptions(
            name='abouthistory',
            options={'ordering': ['-created_at'], 'verbose_name': 'About History', 'verbose_name_plural': 'About History'},
        ),
        # Update HistoryEvent model options
        migrations.AlterModelOptions(
            name='historyevent',
            options={'ordering': ['order', '-year'], 'verbose_name': 'History Event', 'verbose_name_plural': 'History Events'},
        ),
        # Update field help texts
        migrations.AlterField(
            model_name='abouthistory',
            name='content',
            field=models.TextField(help_text='Main history text content (HTML supported)'),
        ),
        migrations.AlterField(
            model_name='abouthistory',
            name='image',
            field=models.ImageField(help_text='Featured image for history section', upload_to='about/history/'),
        ),
        migrations.AlterField(
            model_name='abouthistory',
            name='subtitle',
            field=models.CharField(blank=True, help_text='Optional subtitle', max_length=255),
        ),
        # Create HistoryImage model
        migrations.CreateModel(
            name='HistoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/history/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('year', models.CharField(blank=True, max_length=32)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.abouthistory')),
            ],
            options={'ordering': ['-year', 'order'], 'verbose_name': 'History Image', 'verbose_name_plural': 'History Images'},
        ),
    ]
