
from django.contrib.sitemaps import Sitemap
from .models import Passeio

class PasseioSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Passeio.objects.all()

    def lastmod(self, obj):
        return obj.created
