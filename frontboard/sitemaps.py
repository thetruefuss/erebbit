from django.contrib.sitemaps import Sitemap

from .models import Subject


class SubjectSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Subject.objects.all()

    def lastmod(self, obj):
        return obj.created