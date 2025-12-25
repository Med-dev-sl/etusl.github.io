from django.db import migrations, models


def create_sample_about_history(apps, schema_editor):
    AboutHistory = apps.get_model('api', 'AboutHistory')
    AboutHistory.objects.create(
        title='The History of the Eastern Technical University',
        subtitle='',
        content=(
            "UNIVERSITY OF GHANA was founded in 1948 as the University College of the Gold Coast on the "
            "recommendation of the Asquith Commission, on Higher Education in the then British colonies.\n\n"
            "The Asquith Commission, which was set up in 1943 to investigate Higher Education, recommended "
            "among other things, the setting up of University Colleges in association with the University of London. "
            "This was followed up by a number of separate Commissions in different regions. The West Africa Commission "
            "was under the Chairmanship of the Rt. Hon. Walter Elliot. The Elliot Commission published a majority report "
            "which recommended the establishment of two University Colleges in the Gold Coast (Ghana) and Nigeria, and a "
            "minority report which held that only one University College for the whole of British West Africa was feasible.\n\n"
            "The British Government at first accepted the minority report of the Elliot Commission and decided that a "
            "University College for the whole of British West Africa should be established at Ibadan in Nigeria. However, "
            "the people of the Gold Coast did not accept this recommendation. Led by the scholar and politician, the late "
            "Dr. J.B. Danquah, they urged the Gold Coast Government to inform the British Government that the Gold Coast could "
            "support a University College. Accordingly, the British Government reviewed its decision and agreed to the establishment "
            "of the University College of the Gold Coast.\n\n"
            "The University College of the Gold Coast was founded by Ordinance on August 11, 1948 for the purpose of "
            "providing for and promoting university education, learning and research. Its first Principal was Mr. David "
            "Mowbray Balme, a farsighted and courageous leader dedicated to the promotion of scholarship. By his vision, "
            "industry and single-mindedness of purpose, he built a college and laid the foundations for a sound University "
            "which is now a source of pride. In his ten years of Principalship, he created an institution whose key-note was "
            "orderly living with dignity in a community of scholars.\n\n"
            "From its inception, the University College of the Gold Coast was admitted to the Scheme of Special Relationship, "
            "extended by the University of London to certain English and overseas University Colleges. Under this scheme, the "
            "University College was allowed to teach for the external degree examinations of University of London. It also allowed "
            "the College to modify the London syllabuses to suit local conditions and to take part in the setting and marking of "
            "examinations. The University of London gave final approval for the running of courses and examinations, since it awarded "
            "the degrees.\n\n"
            "For thirteen years, therefore, the University College looked up to two separate institutions in Great Britain: to the "
            "Inter-Universities Council for guidance on its broad policy, and to the University of London for approval and control of "
            "details of degree regulations. The University College benefitted greatly from this arrangement which certainly helped to "
            "maintain its high academic standards.\n\n"
            "In the 1960-61 academic year, the College Council made a request to the Government of Ghana for legislation to constitute "
            "the University College into a University with the power to award its own degrees. The Government appointed an International "
            "Commission to examine the problem. On the recommendations of that Commission, the University of Ghana was set up by an Act "
            "of Parliament on October 1, 1961 (Act 79). The then President of the Republic of Ghana, Dr. Kwame Nkrumah, became the first "
            "Chancellor of the University, with Nana Kobina Nketsia IV, BLitt DPhil (Oxon), Omanhene of Essikado, as the (Interim) "
            "Vice-Chancellor."
        ),
    )


def delete_sample_about_history(apps, schema_editor):
    AboutHistory = apps.get_model('api', 'AboutHistory')
    AboutHistory.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_historyevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, default='History')),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/history/main/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'verbose_name': 'About History', 'verbose_name_plural': 'About History'},
        ),
        migrations.RunPython(create_sample_about_history, delete_sample_about_history),
    ]
