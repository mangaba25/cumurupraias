
from django.contrib.sitemaps import Sitemap
from .models import OndeFicar

class OndeFicarSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return OndeFicar.objects.all()

    def lastmod(self, obj):
        return obj.created
