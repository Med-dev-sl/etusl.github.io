from django.core.management.base import BaseCommand
from api.models import StrategicPlan, StrategicPlanSection


class Command(BaseCommand):
    help = 'Populate strategic plan data'

    def handle(self, *args, **options):
        # Clear existing data
        StrategicPlan.objects.all().delete()
        StrategicPlanSection.objects.all().delete()

        # Create main strategic plan
        plan = StrategicPlan.objects.create(
            title='2018-2025 Strategic Plan',
            summary='What Must Be Done - A strategic vision to navigate new ways to shape the landscape in higher education.'
        )
        self.stdout.write(self.style.SUCCESS(f'Created strategic plan: {plan.title}'))

        # Section 1: Overview
        StrategicPlanSection.objects.create(
            plan=plan,
            heading='Strategic Plan Overview',
            section_type='overview',
            content='''The dynamics of education present both opportunities and challenges — this plan points toward a focus on strategic priorities rooted in the core of Niagara University's strengths in order to navigate new ways to shape the landscape in higher education; affordability and value above all, changing demographics, the economic and workforce needs of the 21st century, and the timeliness of sharing Niagara's mission with emerging populations of students domestically and internationally.

The strategic plan stems from the important framework of the five Strategic Vision Commitments (listed below). The strategic objectives and directions speak to Niagara's influence as we elevate academic excellence, student engagement, the Catholic and Vincentian mission, bi-national opportunity, witnessing the impact of graduates as global citizens of the world.

Through a process of visioning with analysis of internal and external environments, Niagara engaged university-wide councils and committees, sectors and divisions, alumni, students, and the external community, with the aim of gathering relevant input for the University's strategic goals and directions.''',
            order=1
        )

        # Section 2: Vision & Strategic Commitments
        vision_commitments = [
            {
                'title': 'Academic excellence',
                'description': 'founded in interdisciplinary approaches to learning, capitalizing on our strong tradition in liberal arts education and high quality, accredited professional programs.'
            },
            {
                'title': 'Social justice',
                'description': 'with a campus dedicated to diversity and awareness of the local and global environment, and educating students as citizens of the world.'
            },
            {
                'title': 'Mission-driven transformative leadership',
                'description': 'fostering economic and social development with the community and its strategic partners.'
            },
            {
                'title': 'A culture of care',
                'description': 'for the whole person, and an organization strengthened by innovation and shared governance'
            },
            {
                'title': 'An open campus environment',
                'description': 'utilizing cutting-edge technology, and improvements to facilities and outdoor spaces.'
            }
        ]

        StrategicPlanSection.objects.create(
            plan=plan,
            heading='A VIEW TO 2025',
            section_type='vision_commitment',
            subheading='Vision Commitments',
            items=vision_commitments,
            order=2
        )

        # Section 3: Strategic Plan Objectives
        objectives_content = 'The University\'s strategic plan affirms its core strengths, aligns its efforts to build on these strengths while anticipating and responding to challenges, fulfills its commitment to the mission, and ultimately realizes the full potential of Niagara.'

        StrategicPlanSection.objects.create(
            plan=plan,
            heading='STRATEGIC PLAN OBJECTIVES',
            section_type='objectives',
            content=objectives_content,
            order=3
        )

        # Section 4: Objective 1 - Academic Excellence
        objective_1_items = [
            {
                'goal': '1',
                'title': 'Elevate and promote programs of distinction',
                'description': 'Such programs at the undergraduate level include: Psychology, Accounting, Business Management, Nursing, and the Sciences; At the graduate level, programs include: Information Security'
            },
            {
                'goal': '2',
                'title': 'Increase program excellence, sustainability and student interaction with full-time faculty',
                'description': 'by assessing needs and providing resources.'
            },
            {
                'goal': '3',
                'title': 'Revise the general education curriculum',
                'description': 'in a manner that integrates across disciplines both within liberal arts and professional programs.'
            },
            {
                'goal': '4',
                'title': 'Increase research, scholarship, and professional development of faculty, students and staff',
                'description': 'through external funding for support.'
            }
        ]

        StrategicPlanSection.objects.create(
            plan=plan,
            heading='OBJECTIVE 1: ACADEMIC EXCELLENCE',
            subheading='Elevate academic excellence and reputation through student-centered, collaborative, experiential and integrative approaches to learning in preparation for 21st century careers',
            section_type='goals',
            content='Transformational education that integrates the liberal arts and professional study into careers of the 21st century will lead to successful outcomes for graduates, while building the academic profile and reputation of the University. Academic excellence will be defined by the University\'s core strengths in programs and graduate outcomes (value), as well as the quality of students and learning environment.\n\nBuilding from a core of liberal arts and professional study, actions include: revising general education (deep integration with mission and the liberal',
            items=objective_1_items,
            order=4
        )

        # Section 5: Goals for Student Experience
        student_goals = [
            {
                'goal': '1',
                'title': 'Define and establish expectations',
                'description': 'to ensure excellent support, advocacy, and care of the students through processes, training and interactions.'
            },
            {
                'goal': '2',
                'title': 'Invest in residence halls and housing',
                'description': 'athletic and recreational facilities, and the library, which will improve the student learning, residential, and social experience.'
            },
            {
                'goal': '3',
                'title': 'Continuously innovate and advance technology',
                'description': 'across programs and infrastructure.'
            }
        ]

        StrategicPlanSection.objects.create(
            plan=plan,
            heading='GOALS FOR EXCELLENCE IN THE STUDENT EXPERIENCE',
            section_type='goals',
            items=student_goals,
            order=5
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated strategic plan data'))
