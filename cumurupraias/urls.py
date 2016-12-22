"""cumurupraias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from ondecomer.sitemaps import OndeComerSitemap
from home.sitemaps import HomeSitemap
from ondeficar.sitemaps import OndeFicarSitemap
from passeios.sitemaps import PasseioSitemap
from praias.sitemaps import PraiaSitemap
from servicos.sitemaps import ServicoSitemap
from artesanatos.sitemaps import ArtesanatoSitemap

from home import views

sitemaps = {
    'ondecomer': OndeComerSitemap,
    'home':HomeSitemap,
    'ondeficar':OndeFicarSitemap,
    'passios':PasseioSitemap,
    'praias':PraiaSitemap,
    'servicos':ServicoSitemap,
    'artesanatos':ArtesanatoSitemap,

}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name='index'),
    url(r'^como-chegar$', views.comochegar, name='comochegar'),
    url(r'^onde-comer/', include('ondecomer.urls', namespace='ondecomer')),
    url(r'^onde-ficar/', include('ondeficar.urls', namespace='ondeficar')),
    url(r'^passeios/', include('passeios.urls', namespace='passeios')),
    url(r'^compras/', include('artesanatos.urls', namespace='artesanatos')),
    url(r'^servicos/', include('servicos.urls', namespace='servicos')),
    url(r'^praias/', include('praias.urls', namespace='praias')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )



from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.conf.urls.static import static
