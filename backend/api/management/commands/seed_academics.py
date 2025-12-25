from django.core.management.base import BaseCommand
from django.core.files import File
from api.models import AcademicStatistic, AdmissionType, AcademicPage
from pathlib import Path


class Command(BaseCommand):
    help = 'Seed the database with initial academics data'

    def handle(self, *args, **options):
        # Clear existing data
        AcademicStatistic.objects.all().delete()
        AdmissionType.objects.all().delete()
        AcademicPage.objects.all().delete()

        # Create Academic Statistics
        statistics = [
            {
                'statistic_type': 'courses',
                'value': '2000+',
                'label': 'Courses offered',
                'order': 1,
            },
            {
                'statistic_type': 'undergrad',
                'value': '600+',
                'label': 'Undergraduate programmes',
                'order': 2,
            },
            {
                'statistic_type': 'graduate',
                'value': '500+',
                'label': 'Graduate programmes',
                'order': 3,
            },
        ]

        for stat in statistics:
            AcademicStatistic.objects.create(**stat)
            self.stdout.write(
                self.style.SUCCESS(f'Created statistic: {stat["label"]}')
            )

        # Base path to existing images
        media_path = Path(__file__).resolve().parent.parent.parent.parent / 'media' / 'admissions' / '2025' / '12' / '25'

        # Create Admission Types with images
        admissions = [
            {
                'category': 'undergraduate',
                'title': 'Undergraduate Admissions',
                'description': 'Explore our diverse undergraduate programs designed to develop critical thinking and professional skills.',
                'link_url': '#',
                'order': 1,
                'active': True,
                'image_file': 'Laundry_service_design_template_1.jpg',
            },
            {
                'category': 'graduate',
                'title': 'Graduate Admissions',
                'description': 'Advanced degree programs for scholars and professionals seeking specialized knowledge.',
                'link_url': '#',
                'order': 2,
                'active': True,
                'image_file': 'Flyer_-_Innovative_Software_Solutions_2.png',
            },
            {
                'category': 'postfirst',
                'title': 'Post-first degree Admissions',
                'description': 'Continuing education and professional development programs for degree holders.',
                'link_url': '#',
                'order': 3,
                'active': True,
                'image_file': 'Laundry_service_design_template_1.jpg',
            },
        ]

        for admission in admissions:
            image_file = admission.pop('image_file', None)
            admission_obj = AdmissionType.objects.create(**admission)
            
            if image_file and (media_path / image_file).exists():
                with open(media_path / image_file, 'rb') as f:
                    admission_obj.image.save(image_file, File(f), save=True)
                    self.stdout.write(
                        self.style.SUCCESS(f'Assigned image to: {admission["title"]}')
                    )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created admission type: {admission["title"]}')
            )

        # Create Academic Page
        page = AcademicPage.objects.create(
            page_title='Academics',
            hero_subtitle='Academic work is one of the most crucial aspects of the university experience and, therefore, requires discipline and commitment.',
            overview_title='Academic Excellence',
            overview_description='ETU offers a comprehensive range of academic programs across multiple faculties and disciplines. Our commitment to academic excellence ensures that students receive world-class education and mentorship. With experienced faculty and state-of-the-art facilities, we prepare students for success in their chosen fields.',
            nurture_title='Nurturing Success',
            nurture_description='Our serene atmosphere fosters academic excellence, empowering individuals to thrive in their diverse educational pursuits',
            study_with_us_link='#',
            student_handbook_link='#',
            academic_calendar_link='/academics/calendar',
            academic_calendar_title='Academic Calendar',
            academic_calendar_description='See the academic calendar for various schedules and activities for the current academic year',
        )
        self.stdout.write(
            self.style.SUCCESS(f'Created academic page: {page.page_title}')
        )

        self.stdout.write(
            self.style.SUCCESS('Successfully seeded academics data!')
        )
