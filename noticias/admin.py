from django.contrib import admin

# Register your models here.

from .models import Autor, Genero, NoticiaWeb, Noticia

admin.site.register(Noticia)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(NoticiaWeb)