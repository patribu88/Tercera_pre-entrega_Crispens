from django.contrib import admin

from .models import Usuario, Animales, Region, Organizacion, Sexo, Transito

admin.site.register(Usuario)

admin.site.register(Animales)

admin.site.register(Region)

admin.site.register(Organizacion)

admin.site.register(Sexo)

admin.site.register(Transito)