from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from turn.models import Turn, Servise



class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            'index',
            'about',
            'vacancy',
            'tour',
            'contacts',
     
            ]
    def location(self, item):
        return reverse(item)

class TurnSitemap(Sitemap):
    def items(self):
        return Turn.objects.all()

class ServiceSitemap(Sitemap):
    def items(self):
        return Servise.objects.all()