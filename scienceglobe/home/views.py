from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponse


Artigo = apps.get_model('artigos', 'Artigo')
Noticia = apps.get_model('noticias', 'Noticia')
Autor = apps.get_model('artigos', 'Autor')
Forum = apps.get_model('foruns', 'ForumPost')

def home_view(request):

    num_artigos = Artigo.objects.all().count()
    num_noticias = Noticia.objects.all().count()
    num_autores = Autor.objects.count()
    num_foruns = Forum.objects.all().count()

    context = {
        'num_artigos': num_artigos,
        'num_noticias': num_noticias,
        'num_autores': num_autores,
        'num_foruns': num_foruns,
    }
    return render(request, "home.html", context=context)