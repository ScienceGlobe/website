from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponse


Artigo = apps.get_model('artigos', 'Artigo')
NoticiaWeb = apps.get_model('noticias', 'NoticiaWeb')
Genero = apps.get_model('noticias', 'Genero')
Forum = apps.get_model('foruns', 'ForumPost')
ForumGenero = apps.get_model("foruns", "GeneroForum")

def home_view(request):

    genero_economia = Genero.objects.get(name='Economia')
    genero_tecnologia = Genero.objects.get(name='Tecnologia')
    genero_meioAmbiente = Genero.objects.get(name='Meio Ambiente')
    genero_ciencias = Genero.objects.get(name='Ciências')


    forum_genero_duvidas = ForumGenero.objects.get(name= 'Duvidas')
    forum_genero_tecnologia = ForumGenero.objects.get(name= 'Tecnologia')
    forum_genero_curiosidades = ForumGenero.objects.get(name= 'Curiosidades')
    forum_genero_ciencias = ForumGenero.objects.get(name= 'Ciências')
    forum_genero_outros = ForumGenero.objects.get(name= 'Outros')




    num_artigos = Artigo.objects.all().count()



    num_noticias = NoticiaWeb.objects.count()
    num_economia = NoticiaWeb.objects.filter(genero=genero_economia).count()
    num_tecnologia = NoticiaWeb.objects.filter(genero=genero_tecnologia).count()
    num_ciencias = NoticiaWeb.objects.filter(genero=genero_ciencias).count()
    num_meioambiente = NoticiaWeb.objects.filter(genero=genero_meioAmbiente).count()
    



    num_foruns = Forum.objects.all().count()
    num_foruns_curiosidades = Forum.objects.filter(genero=forum_genero_curiosidades).count()
    num_foruns_tecnologia = Forum.objects.filter(genero=forum_genero_tecnologia).count()
    num_foruns_ciencias = Forum.objects.filter(genero =forum_genero_ciencias).count()
    num_foruns_duvidas = Forum.objects.filter(genero=forum_genero_duvidas).count()
    num_foruns_outros = Forum.objects.filter(genero=forum_genero_outros).count()

    context = {
        'num_artigos': num_artigos,
        'num_noticias': num_noticias,
        'num_economia': num_economia,
        'num_tecnologia': num_tecnologia,
        'num_meioambiente': num_meioambiente,
        'num_ciencias': num_ciencias,
        'num_foruns': num_foruns,
        'num_foruns_curiosidades': num_foruns_curiosidades,
        'num_foruns_tecnologia': num_foruns_tecnologia,
        'num_foruns_ciencias': num_foruns_ciencias,
        'num_foruns_duvidas': num_foruns_duvidas,
        'num_foruns_outros': num_foruns_outros,
    }
    return render(request, "home.html", context=context)