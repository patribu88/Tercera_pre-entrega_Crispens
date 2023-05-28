from django.contrib import admin

from .models import Usuario, Animales, Region, Organizacion

admin.site.register(Usuario)

admin.site.register(Animales)

admin.site.register(Region)

admin.site.register(Organizacion)