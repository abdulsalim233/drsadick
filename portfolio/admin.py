from django.contrib import admin
from .models import Profile, ResearchInterest, Publication, Education, Experience, ContactMessage

# Custom Admin Portal Branding
admin.site.site_header = "Surv. Dr. Abubakar Sadiq Mohammed — Admin Portal"
admin.site.site_title = "Dr. Abubakar Sadiq Admin"
admin.site.index_title = "Academic Portfolio & Real Estate Management"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'ghis_number', 'email', 'phone', 'citations_count')
    fieldsets = (
        ('Basic Bio & Headings', {
            'fields': ('name', 'title', 'ghis_number', 'department', 'institution', 'bio', 'profile_image')
        }),
        ('Contact & Links', {
            'fields': ('email', 'phone', 'whatsapp_number', 'office_address', 'citations_count', 'google_scholar_url', 'researchgate_url', 'kpce_directory_url')
        }),
    )

    def has_add_permission(self, request):
        # Prevent creating multiple profile instances
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(ResearchInterest)
class ResearchInterestAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_name', 'display_order', 'is_active', 'read_more_url')
    list_editable = ('display_order', 'is_active')
    search_fields = ('title', 'short_description')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'category', 'citations_count', 'is_featured', 'display_order')
    list_filter = ('year', 'category', 'is_featured')
    search_fields = ('title', 'authors', 'journal_or_conference', 'abstract')
    list_editable = ('citations_count', 'is_featured', 'display_order')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'period', 'display_order')
    list_editable = ('display_order',)
    search_fields = ('degree', 'institution', 'details')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'experience_type', 'period', 'display_order')
    list_filter = ('experience_type',)
    list_editable = ('display_order',)
    search_fields = ('role', 'organization', 'details')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
