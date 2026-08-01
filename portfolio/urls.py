from django.urls import path
from .views import HomeView, PublicationListView, PublicationDetailView, ContactSubmitView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('publications/', PublicationListView.as_view(), name='publication_list'),
    path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication_detail'),
    path('contact/submit/', ContactSubmitView.as_view(), name='contact_submit'),
]
