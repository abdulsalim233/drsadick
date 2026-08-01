from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, View
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Profile, ResearchInterest, Publication, Education, Experience, ContactMessage


def global_profile_context(request):
    """Context processor providing profile data globally to all templates."""
    profile = Profile.objects.first()
    return {'profile': profile}


class HomeView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        
        context['profile'] = profile
        context['research_interests'] = ResearchInterest.objects.filter(is_active=True).order_by('display_order')
        context['featured_publications'] = Publication.objects.filter(is_featured=True).order_by('-year', '-citations_count')[:6]
        if not context['featured_publications'].exists():
            context['featured_publications'] = Publication.objects.all().order_by('-citations_count', '-year')[:6]
            
        context['education_list'] = Education.objects.all().order_by('display_order')
        context['academic_experience'] = Experience.objects.filter(experience_type='academic').order_by('display_order')
        context['industry_experience'] = Experience.objects.filter(experience_type='industry').order_by('display_order')
        context['total_publications_count'] = Publication.objects.count()
        return context


class PublicationListView(ListView):
    model = Publication
    template_name = 'portfolio/publications.html'
    context_object_name = 'publications'
    paginate_by = 10  # Pagination per database optimization rules

    def get_queryset(self):
        queryset = Publication.objects.all().order_by('-year', '-citations_count')
        
        # Category filter
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)
            
        # Search query filter
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q) | queryset.filter(abstract__icontains=q) | queryset.filter(authors__icontains=q)
            
        # Year filter
        year = self.request.GET.get('year')
        if year and year.isdigit():
            queryset = queryset.filter(year=int(year))
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Extract unique categories and years for filter dropdowns/tabs
        context['categories'] = Publication.objects.values_list('category', flat=True).distinct()
        context['years'] = Publication.objects.values_list('year', flat=True).distinct().order_by('-year')
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_year'] = self.request.GET.get('year', '')
        context['search_query'] = self.request.GET.get('q', '')
        return context


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'portfolio/publication_detail.html'
    context_object_name = 'publication'


class ContactSubmitView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not name or not email or not message_text:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Please fill out all required fields.'}, status=400)
            messages.error(request, 'Please fill out all required fields.')
            return redirect('home')

        # Save to Database
        contact = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject or 'Website Inquiry',
            message=message_text
        )

        # Dual Email Notification System
        try:
            profile = Profile.objects.first()
            admin_email = getattr(settings, 'NOTIFICATION_EMAIL', 'drsadick@kpce.edu.gh')

            # 1. Visitor Auto-Reply Confirmation Email
            visitor_subject = f"Thank you for contacting Dr. Abubakar Sadiq Mohammed"
            visitor_context = {
                'name': name,
                'subject': subject or 'Website Inquiry',
                'profile': profile
            }
            visitor_html = render_to_string('emails/visitor_confirmation.html', visitor_context)
            visitor_text = render_to_string('emails/visitor_confirmation.txt', visitor_context)

            send_mail(
                subject=visitor_subject,
                message=visitor_text,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                html_message=visitor_html,
                fail_silently=True
            )

            # 2. Admin Alert Email to Dr. Abubakar
            admin_subject = f"[Website Inquiry] {subject or 'New Message'} from {name}"
            admin_context = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message_text,
                'created_at': contact.created_at
            }
            admin_html = render_to_string('emails/admin_notification.html', admin_context)
            admin_text = render_to_string('emails/admin_notification.txt', admin_context)

            send_mail(
                subject=admin_subject,
                message=admin_text,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[admin_email],
                html_message=admin_html,
                fail_silently=True
            )
        except Exception as e:
            # Suppress email dispatch errors gracefully so user experience is uninterrupted
            pass

        success_msg = "Thank you! Your message has been sent successfully. A confirmation email has been sent to your inbox."

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': success_msg})

        messages.success(request, success_msg)
        return redirect('home')
