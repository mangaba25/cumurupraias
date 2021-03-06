
from django.contrib.sitemaps import Sitemap
from .models import Servico

class ServicoSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Servico.objects.all()

    def lastmod(self, obj):
        return obj.created
