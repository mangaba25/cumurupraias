# coding=utf-8

from django.db import models

from django.db import models
from django.core.urlresolvers import reverse

class CategoryPasseio(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria_Passeio'
        verbose_name_plural = 'Categoria_Passeios'
        ordering = ['name']
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('passeios:category', kwargs={'slug': self.slug})



class Passeio(models.Model):
    name = models.CharField('Nome', max_length=100, blank=True)
    slug = models.SlugField('Identificador', max_length=100, blank=True)
    category = models.ForeignKey('passeios.CategoryPasseio', verbose_name='Categoria_Passeios')
    image_1 = models.ImageField(upload_to='passeios', verbose_name='Imagem_1', null=True, blank=True)
    decription_1 = models.CharField('Descrição-1', max_length=100, blank=True)
    image_2 = models.ImageField(upload_to='passeios', verbose_name='Imagem_2', null=True, blank=True)
    decription_2 = models.CharField('Descrição-2', max_length=100, blank=True)
    image_3 = models.ImageField(upload_to='passeios', verbose_name='Imagem_3', null=True, blank=True)
    decription_3 = models.CharField('Descrição-3', max_length=100, blank=True)
    image_4 = models.ImageField(upload_to='passeios', verbose_name='Imagem_4', null=True, blank=True)
    decription_4 = models.CharField('Descrição-4', max_length=100, blank=True)

    image_5 = models.ImageField(upload_to='passeios', verbose_name='Imagem_5', null=True, blank=True)
    decription_5 = models.CharField('Descrição-5', max_length=100, blank=True)
    image_6 = models.ImageField(upload_to='passeios', verbose_name='Imagem_6', null=True, blank=True)
    decription_6 = models.CharField('Descrição-6', max_length=100, blank=True)
    image_7 = models.ImageField(upload_to='passeios', verbose_name='Imagem_7', null=True, blank=True)
    decription_7 = models.CharField('Descrição-7', max_length=100, blank=True)
    image_8 = models.ImageField(upload_to='passeios', verbose_name='Imagem_8', null=True, blank=True)
    decription_8 = models.CharField('Descrição-8', max_length=100, blank=True)
    image_9 = models.ImageField(upload_to='passeios', verbose_name='Imagem_9', null=True, blank=True)
    decription_9 = models.CharField('Descrição-9', max_length=100, blank=True)
    image_10 = models.ImageField(upload_to='passeios', verbose_name='Imagem_10', null=True, blank=True)
    decription_10 = models.CharField('Descrição-10', max_length=100, blank=True)

    description = models.TextField('Descrição', blank=True)
    address = models.CharField('Endereço', max_length=100, blank=True)
    email = models.EmailField('E-mail', max_length=50, blank=True)
    contact = models.CharField('Contato', max_length=100, blank=True)
    site = models.CharField('Site', max_length=100, blank=True)
    link = models.CharField('link',max_length=120, blank=True)


    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name='Passeio'
        verbose_name_plural = 'Passeios'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('passeios:passeio', kwargs={'slug': self.slug})


class ImagePasseio(models.Model):
    image = models.ImageField(upload_to='images-capa', verbose_name='Imagem', null=True, blank=True)
    decription = models.CharField('Descrição', max_length=100, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name='Imagem_Ondepasseio'



