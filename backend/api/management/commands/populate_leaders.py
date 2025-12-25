from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import LeaderPosition, Leader


class Command(BaseCommand):
    help = 'Populate sample leadership data'

    def handle(self, *args, **options):
        # Create positions if they don't exist
        chancellor_pos, _ = LeaderPosition.objects.get_or_create(
            title='Chancellor',
            defaults={'hierarchy_level': 1, 'order': 1}
        )

        vice_chancellor_pos, _ = LeaderPosition.objects.get_or_create(
            title='Vice-Chancellor',
            defaults={'hierarchy_level': 1, 'order': 2}
        )

        chairperson_pos, _ = LeaderPosition.objects.get_or_create(
            title='Chairperson, UG Council',
            defaults={'hierarchy_level': 2, 'order': 1}
        )

        pro_vc_pos, _ = LeaderPosition.objects.get_or_create(
            title='Pro-Vice-Chancellor (Academic)',
            defaults={'hierarchy_level': 2, 'order': 2}
        )

        registrar_pos, _ = LeaderPosition.objects.get_or_create(
            title='Registrar',
            defaults={'hierarchy_level': 3, 'order': 1}
        )

        bursar_pos, _ = LeaderPosition.objects.get_or_create(
            title='Bursar',
            defaults={'hierarchy_level': 3, 'order': 2}
        )

        # Create sample users and leaders
        users_data = [
            {'username': 'chancellor', 'email': 'chancellor@university.edu', 'first_name': 'Prof.', 'last_name': 'Chancellor'},
            {'username': 'vchancellor', 'email': 'vchancellor@university.edu', 'first_name': 'Prof.', 'last_name': 'Vice-Chancellor'},
            {'username': 'chairperson', 'email': 'chairperson@university.edu', 'first_name': 'Mr.', 'last_name': 'Chairperson'},
            {'username': 'provc', 'email': 'provc@university.edu', 'first_name': 'Prof.', 'last_name': 'Pro-VC'},
            {'username': 'registrar', 'email': 'registrar@university.edu', 'first_name': 'Dr.', 'last_name': 'Registrar'},
            {'username': 'bursar', 'email': 'bursar@university.edu', 'first_name': 'Mr.', 'last_name': 'Bursar'},
        ]

        positions = [
            chancellor_pos,
            vice_chancellor_pos,
            chairperson_pos,
            pro_vc_pos,
            registrar_pos,
            bursar_pos,
        ]

        for user_data, position in zip(users_data, positions):
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                }
            )

            leader, created = Leader.objects.get_or_create(
                user=user,
                defaults={
                    'position': position,
                    'name': f"{user_data['first_name']} {user_data['last_name']}",
                    'bio': f'Biography for {user_data["first_name"]} {user_data["last_name"]}',
                    'email': user_data['email'],
                    'order': positions.index(position) + 1,
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully created leader: {leader.name} - {position.title}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Leader already exists: {leader.name}'
                    )
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated leadership data')
        )
