from django.core.management.base import BaseCommand
from api.models import Affiliate


class Command(BaseCommand):
    help = 'Populate sample affiliates data'

    def handle(self, *args, **options):
        samples = [
            {
                'name': 'Accra College of Medicine, Accra',
                'short_description': 'Private medical college in Accra',
                'description': 'The Accra College of Medicine ("ACM") is a premier private and independent Medical College set up to provide cutting-edge medical education in Ghana. ACM provides world-class medical education that is research oriented and tailored towards solving Ghana and Africa\'s health problems.',
                'website': 'https://acm.edu.gh',
                'contact_email': 'info@acm.edu.gh',
                'contact_phone': '+233-30-000-0000',
                'address': 'Accra, Ghana',
                'order': 1,
            },
            {
                'name': 'Catholic Institute of Business & Technology, Accra',
                'short_description': 'Institute offering business and technology programmes',
                'description': 'Catholic Institute of Business & Technology provides diploma and certificate programmes in business and ICT tailored for industry relevance.',
                'website': 'https://cibt.edu.gh',
                'contact_email': 'contact@cibt.edu.gh',
                'contact_phone': '+233-30-111-1111',
                'address': 'Accra, Ghana',
                'order': 2,
            },
            {
                'name': 'Institute of Accountancy Training - Accra',
                'short_description': 'Accounting and finance training institute',
                'description': 'Institute of Accountancy Training provides professional accountancy training and preparatory courses for ACCA and other accounting certifications.',
                'website': 'https://iat.edu.gh',
                'contact_email': 'info@iat.edu.gh',
                'contact_phone': '+233-30-222-2222',
                'address': 'Accra, Ghana',
                'order': 3,
            },
        ]

        for data in samples:
            obj, created = Affiliate.objects.get_or_create(name=data['name'], defaults=data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created affiliate: {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Affiliate already exists: {obj.name}"))

        self.stdout.write(self.style.SUCCESS('Finished populating affiliates.'))
