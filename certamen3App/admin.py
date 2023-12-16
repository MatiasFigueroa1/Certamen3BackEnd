from django.contrib import admin
from certamen3App.models import *
from django.contrib.auth.models import Permission

admin.site.register(Marca)
admin.site.register(Auto)
admin.site.register(Permission)


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais', 'año', 'marca']

class MarcaAuto(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'año', 'image']
# Register your models here.
