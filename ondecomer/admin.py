from django.contrib import admin

# Register your models here.
from .models import CategoryOndeComer, OndeComer, ImageOndecomer

class CategoryOndeComerAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'created','modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class OndeComerAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category', 'created','modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

class ImageOndecomerAdmin(admin.ModelAdmin):
    list_display = ['image']


admin.site.register(CategoryOndeComer, CategoryOndeComerAdmin)
admin.site.register(OndeComer, OndeComerAdmin)
admin.site.register(ImageOndecomer, ImageOndecomerAdmin)