from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponse



NoticiaWeb = apps.get_model('noticias', 'NoticiaWeb')
Genero = apps.get_model('noticias', 'Genero')
Forum = apps.get_model('foruns', 'ForumPost')
ArtigoWeb = apps.get_model('artigos', 'ArtigoWeb')
ArtigoGenero = apps.get_model('artigos', 'Genero')
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

    artigo_genero_cienciaf = ArtigoGenero.objects.get(name='Ciências físicas e engenharia')
    artigo_genero_cultura = ArtigoGenero.objects.get(name='Cultura')
    artigo_genero_saude = ArtigoGenero.objects.get(name='Saude')
    artigo_genero_tec = ArtigoGenero.objects.get(name='Tecnologia')

    num_artigos = ArtigoWeb.objects.all().count()
    num_ciencias_fisica = ArtigoWeb.objects.filter(genero=artigo_genero_cienciaf).count()
    num_cultura = ArtigoWeb.objects.filter(genero=artigo_genero_cultura).count()
    num_saude = ArtigoWeb.objects.filter(genero=artigo_genero_saude).count()
    num_tec = ArtigoWeb.objects.filter(genero=artigo_genero_tec).count()


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
        'num_ciencias_fisica':num_ciencias_fisica,
        'num_cultura': num_cultura,
        'num_saude': num_saude,
        'num_tec': num_tec,
    }
    return render(request, "home.html", context=context)