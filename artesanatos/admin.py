from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import CategoryArtesanato, Artesanato, ImageArtesanato

class CategoryArtesanatoAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'created','modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class ArtesanatoAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category', 'created','modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

class ImageArtesanatoAdmin(admin.ModelAdmin):
    list_display = ['image']



admin.site.register(CategoryArtesanato, CategoryArtesanatoAdmin)
admin.site.register(Artesanato, ArtesanatoAdmin)
admin.site.register(ImageArtesanato, ImageArtesanatoAdmin)

