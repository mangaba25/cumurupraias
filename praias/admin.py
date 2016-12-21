from django.contrib import admin

# Register your models here.
from .models import CategoryPraia, Praia, ImagePraia

class CategoryPraiaAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'created','modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class PraiaAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category', 'created','modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

class ImagePraiaAdmin(admin.ModelAdmin):
    list_display = ['image']



admin.site.register(CategoryPraia, CategoryPraiaAdmin)
admin.site.register(Praia, PraiaAdmin)
admin.site.register(ImagePraia, ImagePraiaAdmin)

