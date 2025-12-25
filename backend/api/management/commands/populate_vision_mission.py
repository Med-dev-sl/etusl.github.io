from django.core.management.base import BaseCommand
from api.models import VisionMission, CoreValue, StrategicPriority, PriorityItem


class Command(BaseCommand):
    help = 'Populate VisionMission, CoreValues, and StrategicPriorities with sample data'

    def handle(self, *args, **options):
        # Create VisionMission
        vm, created = VisionMission.objects.get_or_create(
            id=1,
            defaults={
                'vision_title': 'Our Vision',
                'vision_text': 'To achieve global impact through innovative research, teaching and learning, using a technology-driven and people-centred approach.',
                'mission_title': 'Our Mission',
                'mission_text': 'To create an enabling environment that makes the University increasingly relevant to national and global development through cutting-edge research and quality teaching and learning.',
                'image_alt': 'University Campus',
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created VisionMission'))
        else:
            self.stdout.write('VisionMission already exists')

        # Create CoreValues
        core_values_data = [
            {
                'title': 'Integrity',
                'description': 'We demand the highest standard of ourselves to earn the trust of others.',
                'order': 0,
            },
            {
                'title': 'Commitment',
                'description': 'We are committed to knowledge generation that positively impacts the lives of those within and outside our University community.',
                'order': 1,
            },
            {
                'title': 'Respect',
                'description': 'We provide others with a world-class experience that demonstrates our value for the diversity and contributions of the members of our community.',
                'order': 2,
            },
            {
                'title': 'Loyalty',
                'description': 'We demonstrate a strong resolve to give back selflessly to our University.',
                'order': 3,
            },
        ]

        for value_data in core_values_data:
            cv, created = CoreValue.objects.get_or_create(
                title=value_data['title'],
                defaults=value_data,
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created CoreValue: {value_data["title"]}'))

        # Create StrategicPriority
        sp, created = StrategicPriority.objects.get_or_create(
            id=1,
            defaults={
                'title': 'Our Strategic Priorities',
                'image_alt': 'University Strategic Initiatives',
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created StrategicPriority'))

        # Create PriorityItems
        priority_items_data = [
            {
                'text': 'Transformative Student Experience',
                'order': 0,
            },
            {
                'text': 'Impactful Research',
                'order': 1,
            },
            {
                'text': 'Commitment to our Faculty and Staff',
                'order': 2,
            },
            {
                'text': 'Engagement and Partnerships',
                'order': 3,
            },
            {
                'text': 'Sustainable Resource Mobilisation and Stewardship.',
                'order': 4,
            },
        ]

        for item_data in priority_items_data:
            pi, created = PriorityItem.objects.get_or_create(
                priority=sp,
                text=item_data['text'],
                defaults=item_data,
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created PriorityItem: {item_data["text"]}'))

        self.stdout.write(self.style.SUCCESS('\n✓ All data populated successfully!'))
