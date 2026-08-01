from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from portfolio.models import Profile, ResearchInterest, Publication, Education, Experience, ContactMessage

class PortfolioModelTests(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            name="Surv. Dr. Abubakar Sadiq Mohammed (PhD)",
            title="Lecturer in Facilities Management",
            ghis_number="GhIS Member: VESD – 2599",
            citations_count=179
        )
        self.pub = Publication.objects.create(
            title="Emerging technologies for transforming mosques into smart buildings",
            authors="AS Mohammed",
            year=2024,
            category="Smart FM",
            citations_count=18,
            is_featured=True
        )

    def test_profile_creation_and_str(self):
        self.assertEqual(str(self.profile), "Surv. Dr. Abubakar Sadiq Mohammed (PhD)")
        self.assertEqual(self.profile.citations_count, 179)

    def test_publication_creation_and_str(self):
        self.assertEqual(str(self.pub), "Emerging technologies for transforming mosques into smart buildings (2024)")
        self.assertTrue(self.pub.is_featured)


class PortfolioViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            name="Surv. Dr. Abubakar Sadiq Mohammed (PhD)",
            title="Lecturer in Facilities Management",
            ghis_number="GhIS Member: VESD – 2599"
        )
        self.pub1 = Publication.objects.create(
            title="Technology integration on infrastructure",
            authors="AS Mohammed",
            year=2023,
            category="Educational Infrastructure",
            citations_count=21,
            is_featured=True
        )
        self.pub2 = Publication.objects.create(
            title="Facilities managers vs. mosque management committees",
            authors="AS Mohammed",
            year=2023,
            category="Mosque Operations",
            citations_count=19
        )

    def test_home_page_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Abubakar Sadiq Mohammed")
        self.assertContains(response, "GhIS Member: VESD – 2599")

    def test_publication_list_page_returns_200_and_filters(self):
        response = self.client.get(reverse('publication_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Technology integration on infrastructure")
        
        # Test category filtering
        filter_response = self.client.get(reverse('publication_list') + '?category=Mosque+Operations')
        self.assertEqual(filter_response.status_code, 200)
        self.assertContains(filter_response, "Facilities managers vs. mosque management committees")

    def test_contact_form_submission_triggers_dual_emails(self):
        post_data = {
            'name': 'Prof. John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Research Inquiry',
            'message': 'I would like to collaborate on smart building research.'
        }
        response = self.client.post(reverse('contact_submit'), post_data)
        
        # Verify contact saved in database
        self.assertEqual(ContactMessage.objects.count(), 1)
        contact = ContactMessage.objects.first()
        self.assertEqual(contact.name, 'Prof. John Doe')
        
        # Verify 2 emails sent (Visitor confirmation + Admin notification)
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].to, ['johndoe@example.com'])
        self.assertIn("Thank you for contacting", mail.outbox[0].subject)

    def test_404_page_rendering(self):
        response = self.client.get('/non-existent-page-url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, "Page Not Found", status_code=404)

