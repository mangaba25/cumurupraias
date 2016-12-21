# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse

class CategoryArtesanato(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria_Artesanato'
        verbose_name_plural = 'Categoria_Artesanato'
        ordering = ['name']
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artesanatos:category', kwargs={'slug': self.slug})



class Artesanato(models.Model):
    name = models.CharField('Nome', max_length=100, blank=True)
    slug = models.SlugField('Identificador', max_length=100, blank=True)
    category = models.ForeignKey('artesanatos.CategoryArtesanato', verbose_name='Categoria_Artesanato')
    image_1 = models.ImageField(upload_to='artesanatos', verbose_name='Imagem_1', null=True, blank=True)
    decription_1 = models.CharField('Descrição-1', max_length=100, blank=True)
    image_2 = models.ImageField(upload_to='artesanatos', verbose_name='Imagem_2', null=True, blank=True)
    decription_2 = models.CharField('Descrição-2', max_length=100, blank=True)
    image_3 = models.ImageField(upload_to='artesanatos', verbose_name='Imagem_3', null=True, blank=True)
    decription_3 = models.CharField('Descrição-3', max_length=100, blank=True)
    image_4 = models.ImageField(upload_to='artesanatos', verbose_name='Imagem_4', null=True, blank=True)
    decription_4 = models.CharField('Descrição-4', max_length=100, blank=True)

    description = models.TextField('Descrição', blank=True)
    address = models.CharField('Endereço', max_length=100, blank=True)
    email = models.EmailField('E-mail', max_length=50, blank=True)
    contact = models.CharField('Contato', max_length=100, blank=True)
    site = models.CharField('Site', max_length=100, blank=True)
    link = models.CharField('link',max_length=120, blank=True)


    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name='Artesanato'
        verbose_name_plural = 'Artesanatos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artesanatos:artesanato', kwargs={'slug': self.slug})

class ImageArtesanato(models.Model):
    image = models.ImageField(upload_to='images-capa', verbose_name='Imagem', null=True, blank=True)
    decription = models.CharField('Descrição', max_length=100, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name='Imagem_Artesanato'



