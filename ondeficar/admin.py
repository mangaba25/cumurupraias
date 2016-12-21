from django.contrib import admin

# Register your models here.
from .models import CategoryOndeFicar, OndeFicar, ImageOndeficar

class CategoryOndeFicarAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'created','modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class OndeFicarAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category', 'created','modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

class ImageOndeficarAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(CategoryOndeFicar, CategoryOndeFicarAdmin)
admin.site.register(OndeFicar, OndeFicarAdmin)
admin.site.register(ImageOndeficar, ImageOndeficarAdmin)