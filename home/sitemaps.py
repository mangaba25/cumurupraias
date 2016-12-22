
from django.contrib.sitemaps import Sitemap
from .models import Home

class HomeSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Home.objects.all()

    def lastmod(self, obj):
        return obj.created
