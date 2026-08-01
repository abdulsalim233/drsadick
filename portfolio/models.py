from django.db import models
from django.urls import reverse

class Profile(models.Model):
    name = models.CharField(max_length=150, default="Surv. Dr. Abubakar Sadiq Mohammed (PhD)")
    title = models.CharField(max_length=200, default="Lecturer & Professional Facilities Management Surveyor")
    ghis_number = models.CharField(max_length=100, default="GhIS Member: VESD – 2599")
    department = models.CharField(max_length=200, default="Department of Building Technology")
    institution = models.CharField(max_length=200, default="Accra Technical University, Ghana")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField(default="drsadick@kpce.edu.gh")
    phone = models.CharField(max_length=30, default="+233544966668")
    whatsapp_number = models.CharField(max_length=30, default="233544966668", help_text="Format: 233544966668 without + sign")
    office_address = models.CharField(max_length=255, default="Kibi Presbyterian College of Education & Accra Technical University")
    citations_count = models.IntegerField(default=179, db_index=True)
    google_scholar_url = models.URLField(default="https://scholar.google.com/citations?user=hMUoZnQAAAAJ&hl=en")
    researchgate_url = models.URLField(default="https://www.researchgate.net/profile/Abubakar-Mohammed-27")
    kpce_directory_url = models.URLField(default="https://directory.kpce.edu.gh/personnel/surv-mohammed-abubakar-sadiq/")
    
    class Meta:
        verbose_name = "Profile Information"
        verbose_name_plural = "Profile Information"

    def __str__(self):
        return self.name


class ResearchInterest(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField()
    icon_name = models.CharField(max_length=50, default="building", help_text="Icon identifier (e.g. building, cpu, mosque, shield, users, wrench)")
    read_more_url = models.URLField(blank=True, null=True, help_text="Direct link to ResearchGate or Scholar paper on this topic")
    display_order = models.IntegerField(default=0, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Research Interest"
        verbose_name_plural = "Research Interests"

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=350)
    authors = models.CharField(max_length=350)
    journal_or_conference = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(db_index=True)
    citations_count = models.IntegerField(default=0, db_index=True)
    category = models.CharField(max_length=100, db_index=True, help_text="Category tag e.g. Smart FM, Mosque Operations, Healthcare, Education")
    abstract = models.TextField(blank=True)
    google_scholar_link = models.URLField(blank=True, null=True)
    researchgate_link = models.URLField(blank=True, null=True)
    doi_link = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    display_order = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['-year', '-citations_count', 'display_order']
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self):
        return f"{self.title} ({self.year})"

    def get_absolute_url(self):
        return reverse('publication_detail', kwargs={'pk': self.pk})


class Education(models.Model):
    degree = models.CharField(max_length=200) # e.g. Ph.D. in Land Management & Governance
    institution = models.CharField(max_length=200) # e.g. Kwame Nkrumah University of Science and Technology (KNUST)
    location = models.CharField(max_length=150, default="Ghana")
    period = models.CharField(max_length=100) # e.g. Ongoing / 2023 - Present
    details = models.TextField(blank=True)
    display_order = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Education History"
        verbose_name_plural = "Education Histories"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Experience(models.Model):
    TYPE_CHOICES = (
        ('academic', 'Academic & Teaching'),
        ('industry', 'Professional Surveying & Industry'),
    )
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=150, default="Ghana")
    period = models.CharField(max_length=100)
    experience_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='academic', db_index=True)
    details = models.TextField(blank=True)
    display_order = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Professional Experience"
        verbose_name_plural = "Professional Experiences"

    def __str__(self):
        return f"{self.role} at {self.organization}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    is_read = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
