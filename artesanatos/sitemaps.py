
from django.contrib.sitemaps import Sitemap
from .models import Artesanato

class ArtesanatoSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Artesanato.objects.all()

    def lastmod(self, obj):
        return obj.created
