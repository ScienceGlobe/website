from django.shortcuts import render
from django.apps import apps
from django.db.models import Q

artigo=apps.get_model('artigos', 'Artigo')
noticia=apps.get_model('noticias', 'NoticiaWeb')
forum=apps.get_model('foruns', 'ForumPost')

def search(request):
    query = request.GET.get('q')
    if query:
        artigo_results = artigo.objects.filter(Q(title__icontains=query) | Q(texto__icontains=query))
        noticia_results = noticia.objects.filter(Q(title__icontains=query) | Q(corpo__icontains=query))
        forum_results = forum.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
        results = {
            'artigo_results': artigo_results,
            'noticia_results': noticia_results,
            'forum_results': forum_results,
        }
    else:
        results = {}

    return render(request, 'search/search_results.html', {'results': results, 'query': query})


 