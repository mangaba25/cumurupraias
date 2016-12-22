
from django.contrib.sitemaps import Sitemap
from .models import Praia

class PraiaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Praia.objects.all()

    def lastmod(self, obj):
        return obj.created
