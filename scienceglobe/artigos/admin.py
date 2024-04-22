from django.contrib import admin

# Register your models here.

from .models import Autor, Tipo, Artigo

admin.site.register(Artigo)
admin.site.register(Autor)
admin.site.register(Tipo)