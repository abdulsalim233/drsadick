from django.core.management.base import BaseCommand
from portfolio.models import Profile, ResearchInterest, Publication, Education, Experience

class Command(BaseCommand):
    help = 'Seeds database with real profile and academic data for Dr. Abubakar Sadiq Mohammed'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # Profile
        profile, created = Profile.objects.update_or_create(
            id=1,
            defaults={
                'name': 'Surv. Dr. Abubakar Sadiq Mohammed (PhD)',
                'title': 'Lecturer & Professional Facilities Management Surveyor',
                'ghis_number': 'GhIS Member: VESD – 2599',
                'department': 'Department of Building Technology',
                'institution': 'Accra Technical University, Ghana',
                'bio': 'Surv. Dr. Abubakar Sadiq Mohammed is a dedicated Facilities and Real Estate Professional, Lecturer at Accra Technical University, and PhD Candidate in Land Management and Governance at KNUST. With extensive expertise in both soft and hard facilities management, estate valuation, and real estate services, his research focuses on smart building technologies, religious facility management, disaster preparedness, and gender dynamics in facilities management across Africa.',
                'email': 'drsadick@kpce.edu.gh',
                'phone': '+233 54 496 6668',
                'whatsapp_number': '233544966668',
                'office_address': 'Department of Building Technology, Accra Technical University & KPCE, Ghana',
                'citations_count': 179,
                'google_scholar_url': 'https://scholar.google.com/citations?user=hMUoZnQAAAAJ&hl=en',
                'researchgate_url': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'kpce_directory_url': 'https://directory.kpce.edu.gh/personnel/surv-mohammed-abubakar-sadiq/',
            }
        )

        # Research Interests
        interests_data = [
            {
                'title': 'Smart Building & IoT Facilities Management',
                'short_description': 'Integrating IoT solutions, smart sensors, and automated building management systems to transform traditional infrastructure into intelligent, sustainable facilities.',
                'icon_name': 'cpu',
                'read_more_url': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'display_order': 1,
            },
            {
                'title': 'Religious Facilities Management (Mosque Operations)',
                'short_description': 'Evaluating estate management practices, facility maintenance, and technology integration in central and campus mosques to enhance worshipper well-being and operational efficiency.',
                'icon_name': 'mosque',
                'read_more_url': 'https://scholar.google.com/citations?user=hMUoZnQAAAAJ&hl=en',
                'display_order': 2,
            },
            {
                'title': 'Sustainable Healthcare & Educational Infrastructure',
                'short_description': 'Assessing maintenance practices, energy efficiency, and disaster preparedness in higher education institutions and healthcare facilities across Ghana.',
                'icon_name': 'building',
                'read_more_url': 'https://directory.kpce.edu.gh/personnel/surv-mohammed-abubakar-sadiq/',
                'display_order': 3,
            },
            {
                'title': 'Gender Inclusivity & Workplace Efficiency in FM',
                'short_description': 'Examining gender disparities, pre-service teacher satisfaction levels, and the impactful role of female professionals in facilities management.',
                'icon_name': 'users',
                'read_more_url': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'display_order': 4,
            },
        ]

        for item in interests_data:
            ResearchInterest.objects.update_or_create(
                title=item['title'],
                defaults=item
            )

        # Publications
        pubs_data = [
            {
                'title': 'Technology integration on infrastructure to support educational needs in a college in Ghana',
                'authors': 'AS Mohammed, et al.',
                'journal_or_conference': 'Journal of Facilities Management',
                'year': 2023,
                'citations_count': 21,
                'category': 'Educational Infrastructure',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:4JMBOYKVnBMC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': True,
                'display_order': 1,
            },
            {
                'title': 'Facilities managers vs. mosque management committees: evaluating the need for professional facilities management in mosque operations',
                'authors': 'AS Mohammed, C Amoah, J Abbas',
                'journal_or_conference': 'Journal of Cultural Heritage Management and Sustainable Development',
                'year': 2023,
                'citations_count': 19,
                'category': 'Mosque Operations',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:e5wmG9Sq2KIC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': True,
                'display_order': 2,
            },
            {
                'title': 'Integration of technology in decision-making in university facilities management: a literature review',
                'authors': 'AS Mohammed, T Alhassan',
                'journal_or_conference': 'Property Management Journal',
                'year': 2022,
                'citations_count': 18,
                'category': 'Smart FM',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:-f6ydRqryjwC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': True,
                'display_order': 3,
            },
            {
                'title': 'Emerging technologies for transforming mosques into smart buildings: a systematic literature review',
                'authors': 'AS Mohammed, I Aidoo, J Agbevade',
                'journal_or_conference': 'Smart and Sustainable Built Environment',
                'year': 2024,
                'citations_count': 18,
                'category': 'Smart FM',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:ZeXyd9-uunAC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': True,
                'display_order': 4,
            },
            {
                'title': 'Assessment of user awareness of electricity consumption based on norm activation model: the study of a public university in Ghana',
                'authors': 'AS Mohammed, TO Ayodele',
                'journal_or_conference': 'Energy and Buildings',
                'year': 2023,
                'citations_count': 16,
                'category': 'Energy & Sustainability',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:Wp0gIr-vW9MC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': False,
                'display_order': 5,
            },
            {
                'title': 'Examining the complexities of estate management practices in Central mosques: a case study of Kumasi Central mosque in Ghana',
                'authors': 'AS Mohammed, AN Benyi',
                'journal_or_conference': 'Journal of Building Performance',
                'year': 2023,
                'citations_count': 16,
                'category': 'Mosque Operations',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:aqlVkmm33-oC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': False,
                'display_order': 6,
            },
            {
                'title': 'Examining gender disparities in pre-service teachers satisfaction levels across educational facilities',
                'authors': 'AS Mohammed, AT Bobie',
                'journal_or_conference': 'International Journal of Educational Management',
                'year': 2023,
                'citations_count': 14,
                'category': 'Gender & Satisfaction',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:4DMP91E08xMC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': False,
                'display_order': 7,
            },
            {
                'title': 'Enhancing disaster preparedness in higher education institutions in Ghana: the role of facility managers',
                'authors': 'AS Mohammed, S Forson',
                'journal_or_conference': 'Disaster Prevention and Management',
                'year': 2023,
                'citations_count': 12,
                'category': 'Educational Infrastructure',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:HDshCWvjkbEC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': False,
                'display_order': 8,
            },
            {
                'title': 'Assessment of Maintenance Practices in Health Care Institutions in Ghana: A Study of Bekwai Municipal Hospital',
                'authors': 'AS Mohammed, FD Issah',
                'journal_or_conference': 'Journal of Health Organization and Management',
                'year': 2022,
                'citations_count': 12,
                'category': 'Healthcare FM',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:M3NEmzRMIkIC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': False,
                'display_order': 9,
            },
            {
                'title': 'Bibliometric analysis of innovative technology use in sustainable facilities management for smart city development',
                'authors': 'AS Mohammed, K Kajimo-Shakantu',
                'journal_or_conference': 'Sustainable Cities and Society',
                'year': 2024,
                'citations_count': 9,
                'category': 'Smart FM',
                'google_scholar_link': 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hMUoZnQAAAAJ&citation_for_view=hMUoZnQAAAAJ:QIV2ME_5wuYC',
                'researchgate_link': 'https://www.researchgate.net/profile/Abubakar-Mohammed-27',
                'is_featured': True,
                'display_order': 10,
            },
        ]

        for item in pubs_data:
            Publication.objects.update_or_create(
                title=item['title'],
                defaults=item
            )

        # Education
        edu_data = [
            {
                'degree': 'Ph.D. in Land Management and Governance',
                'institution': 'Kwame Nkrumah University of Science and Technology (KNUST)',
                'location': 'Kumasi, Ghana',
                'period': '2023 - Present (Pursuing)',
                'details': 'Focusing on advanced land governance, property science, and smart facilities management strategies for developing nations.',
                'display_order': 1,
            },
            {
                'degree': 'M.Sc. in Facilities Management',
                'institution': 'Kwame Nkrumah University of Science and Technology (KNUST)',
                'location': 'Kumasi, Ghana',
                'period': 'Completed',
                'details': 'Specialized in strategic facility maintenance, healthcare and educational building operations, and energy efficiency models.',
                'display_order': 2,
            },
            {
                'degree': 'B.Tech. in Estate Management',
                'institution': 'Kumasi Technical University (KsTU)',
                'location': 'Kumasi, Ghana',
                'period': 'Completed',
                'details': 'Graduated with honors, focusing on real estate valuation, property rating, property development, and building maintenance.',
                'display_order': 3,
            },
            {
                'degree': 'HND in Estate Management',
                'institution': 'Kumasi Technical University (KsTU)',
                'location': 'Kumasi, Ghana',
                'period': 'Completed',
                'details': 'Foundational qualifications in estate surveying, valuation methods, land law, and building technology.',
                'display_order': 4,
            },
        ]

        for item in edu_data:
            Education.objects.update_or_create(
                degree=item['degree'],
                institution=item['institution'],
                defaults=item
            )

        # Experience
        exp_data = [
            {
                'role': 'Lecturer in Facilities Management',
                'organization': 'Accra Technical University (ATU)',
                'location': 'Accra, Ghana',
                'period': 'Present',
                'experience_type': 'academic',
                'details': 'Department of Building Technology. Lecturing undergraduate students in Facilities Management, Property Valuation, and Building Maintenance.',
                'display_order': 1,
            },
            {
                'role': 'Senior Estate Management Assistant',
                'organization': 'Kibi Presbyterian College of Education (KPCE)',
                'location': 'Kibi, Ghana',
                'period': '2019 - Present',
                'experience_type': 'academic',
                'details': 'Managing college real estate assets, structural maintenance, facility planning, disaster preparedness, and estate administration.',
                'display_order': 2,
            },
            {
                'role': 'Professional Surveyor (GhIS Member: VESD – 2599)',
                'organization': 'Ghana Institution of Surveyors',
                'location': 'Accra, Ghana',
                'period': '2020 - Present',
                'experience_type': 'industry',
                'details': 'Certified professional practice under the Valuation and Estate Surveying Division (VESD).',
                'display_order': 3,
            },
            {
                'role': 'Valuation & Estate Surveyor (Part-Time)',
                'organization': 'Suhum Rural Bank Ltd',
                'location': 'Suhum, Ghana',
                'period': 'Previous',
                'experience_type': 'industry',
                'details': 'Conducting property valuations, collateral asset assessments, and estate advisory for banking operations.',
                'display_order': 4,
            },
            {
                'role': 'Facilities Officer (Part-Time)',
                'organization': 'Mas 17 Real Estates',
                'location': 'Ghana',
                'period': 'Previous',
                'experience_type': 'industry',
                'details': 'Overseeing commercial real estate maintenance, tenant relations, and operational facility service delivery.',
                'display_order': 5,
            },
        ]

        for item in exp_data:
            Experience.objects.update_or_create(
                role=item['role'],
                organization=item['organization'],
                defaults=item
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with Dr. Abubakar Sadiq Mohammed data!'))
