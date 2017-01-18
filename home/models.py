from django.db import models
from django.core.urlresolvers import reverse

class Home(models.Model):
    phrase = models.CharField('Frase', max_length=120, blank=True)
    slug = models.SlugField('Identificador',unique=True)
    image = models.ImageField(upload_to='imagem-index', null=True, blank=True)
    description = models.CharField('Descrição',max_length=120, blank=True)
    link = models.CharField('link',max_length=120, blank=True)
    palavralink = models.CharField('palavra-link',max_length=120, blank=True)
    subtitle = models.CharField('Legenda', max_length=100, blank=True)
    subtitlelink = models.CharField('subtitle-link',max_length=120, blank=True)
    subtitlepalavralink = models.CharField('palavra-subtitle-link',max_length=120, blank=True)
    content = models.TextField('Conteudo', blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Home'

    def get_absolute_url(self):
        return reverse('index')

class Dica(models.Model):
    dica = models.CharField('Frase', max_length=120)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Dica'

class Aviso(models.Model):
    aviso = models.CharField('Frase', max_length=120)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Aviso'



