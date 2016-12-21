from django.contrib import admin

# Register your models here.
from .models import CategoryPasseio, Passeio, ImagePasseio

class CategoryPasseioAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'created','modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class PasseioAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category', 'created','modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

class ImagePasseioAdmin(admin.ModelAdmin):
    list_display = ['image']


admin.site.register(CategoryPasseio, CategoryPasseioAdmin)
admin.site.register(Passeio, PasseioAdmin)
admin.site.register(ImagePasseio, ImagePasseioAdmin)


