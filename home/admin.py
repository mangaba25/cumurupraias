from django.contrib import admin

# Register your models here.
from .models import Dica, Aviso, Home

class DicaAdmin(admin.ModelAdmin):
    list_display = ['dica','created','modified']
    search_fields = ['dica']
    list_filter = ['created', 'modified']

class AvisoAdmin(admin.ModelAdmin):
    list_display = ['aviso', 'created','modified']
    search_fields = ['aviso']
    list_filter = ['created', 'modified']

class HomeAdmin(admin.ModelAdmin):
    list_display = ['phrase', 'created','modified']
    search_fields = ['aviso']
    list_filter = ['created', 'modified']


admin.site.register(Aviso, AvisoAdmin)
admin.site.register(Dica, DicaAdmin)
admin.site.register(Home, HomeAdmin)


