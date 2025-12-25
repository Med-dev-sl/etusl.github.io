from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from api.models import PolicyDocument


class Command(BaseCommand):
    help = 'Populate sample policy documents'

    def handle(self, *args, **options):
        policies = [
            {
                'title': 'The Harmonisation of Assessment Processes in the University of Sierra Leone',
                'short_description': 'Assessment guidelines and policy',
                'filename': 'harmonisation-assessment.pdf',
            },
            {
                'title': 'Revised University of Sierra Leone Academic, Research and Students policy Nov 2018',
                'short_description': 'Academic and research policy',
                'filename': 'revised-university-policy.pdf',
            },
            {
                'title': 'Quality Assurance and Performance Management Policy – 2018',
                'short_description': 'Quality assurance framework',
                'filename': 'quality-assurance-policy.pdf',
            },
            {
                'title': 'University of Sierra Leone Conflict of Interest Policy',
                'short_description': 'Conflict of interest guidelines',
                'filename': 'conflict-of-interest.pdf',
            },
            {
                'title': 'Financial Management Policy -Oct 2018',
                'short_description': 'Financial regulations and guidelines',
                'filename': 'financial-management.pdf',
            },
            {
                'title': 'Human Resource and Administrative Policy',
                'short_description': 'HR and administration framework',
                'filename': 'human-resource-policy.pdf',
            },
            {
                'title': 'ICT Policy – Oct 2018',
                'short_description': 'Information and communications technology policy',
                'filename': 'ict-policy.pdf',
            },
            {
                'title': 'Strategic Plan',
                'short_description': 'University strategic direction and priorities',
                'filename': 'strategic-plan.pdf',
            },
        ]

        for idx, policy_data in enumerate(policies, start=1):
            # Create a fake PDF file content (just placeholder)
            file_content = ContentFile(b'%PDF-1.4\n%Fake PDF content for ' + policy_data['filename'].encode())
            
            policy, created = PolicyDocument.objects.get_or_create(
                title=policy_data['title'],
                defaults={
                    'short_description': policy_data['short_description'],
                    'order': idx,
                }
            )
            
            if created:
                # Only set the file if newly created
                policy.file.save(policy_data['filename'], file_content, save=True)
                self.stdout.write(self.style.SUCCESS(f'Created policy: {policy.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Policy already exists: {policy.title}'))

        self.stdout.write(self.style.SUCCESS('Finished populating policies.'))
