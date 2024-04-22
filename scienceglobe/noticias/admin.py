from django.contrib import admin

# Register your models here.

from .models import Autor, Genero, Noticia

admin.site.register(Noticia)
admin.site.register(Autor)
admin.site.register(Genero)