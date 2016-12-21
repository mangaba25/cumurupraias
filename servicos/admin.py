from django.contrib import admin

# Register your models here.
from .models import CategoryServico, Servico, ImageServico

class CategoryServicoAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'created','modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class ServicoAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category', 'created','modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

class ImageServicoAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(CategoryServico, CategoryServicoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(ImageServico, ImageServicoAdmin)