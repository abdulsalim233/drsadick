from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Publication

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['home', 'publication_list']

    def location(self, item):
        return reverse(item)


class PublicationSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return Publication.objects.all()
