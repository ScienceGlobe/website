from django.contrib import admin

# Register your models here.

from .models import Autor, Tipo, Artigo, ArtigoWeb

admin.site.register(Artigo)
admin.site.register(Autor)
admin.site.register(Tipo)
admin.site.register(ArtigoWeb)