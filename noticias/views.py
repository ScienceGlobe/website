from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticia, NoticiaWeb

# Create your views here.

def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "noticias.html", {})

class NoticiasView(ListView):
    model = NoticiaWeb
    paginate_by = 5
    context_object_name = 'noticiaweb_list'

class NoticiaDetailView(DetailView):
    model = NoticiaWeb
    template_name = 'noticias/noticiaweb_detail.html'

def filtrar_noticias_por_genero(request, genero):
    
    noticias = NoticiaWeb.objects.filter(genero__name=genero)
    
    return render(request, 'noticias/noticiaweb_por_genero.html', {'noticias': noticias, 'genero': genero})