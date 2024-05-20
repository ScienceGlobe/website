from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponse


Artigo = apps.get_model('artigos', 'Artigo')
NoticiaWeb = apps.get_model('noticias', 'NoticiaWeb')
Genero = apps.get_model('noticias', 'Genero')
Forum = apps.get_model('foruns', 'ForumPost')

def home_view(request):

    genero_economia = Genero.objects.get(name='Economia')
    genero_tecnologia = Genero.objects.get(name='Tecnologia')
    genero_meioAmbiente = Genero.objects.get(name='Meio Ambiente')
    genero_ciencias = Genero.objects.get(name='Ciências')




    num_artigos = Artigo.objects.all().count()



    num_noticias = NoticiaWeb.objects.count()
    num_economia = NoticiaWeb.objects.filter(genero=genero_economia).count()
    num_tecnologia = NoticiaWeb.objects.filter(genero=genero_tecnologia).count()
    num_ciencias = NoticiaWeb.objects.filter(genero=genero_ciencias).count()
    num_meioambiente = NoticiaWeb.objects.filter(genero=genero_meioAmbiente).count()
    



    num_foruns = Forum.objects.all().count()

    context = {
        'num_artigos': num_artigos,
        'num_noticias': num_noticias,
        'num_economia': num_economia,
        'num_tecnologia': num_tecnologia,
        'num_meioambiente': num_meioambiente,
        'num_ciencias': num_ciencias,
        'num_foruns': num_foruns,
    }
    return render(request, "home.html", context=context)