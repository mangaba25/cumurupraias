
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listar, name='listar'),
    url(r'^(?P<slug>[\w_-]+)$', views.artesanato, name='artesanato'),
]