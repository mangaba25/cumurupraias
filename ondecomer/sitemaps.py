
from django.contrib.sitemaps import Sitemap
from .models import OndeComer

class OndeComerSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return OndeComer.objects.all()

    def lastmod(self, obj):
        return obj.created
