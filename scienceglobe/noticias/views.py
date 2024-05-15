from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticia, NoticiaWeb
from .scripts import scrape_noticias

# Create your views here.

def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "noticias.html", {})

class NoticiasView(ListView):
    model = NoticiaWeb
    context_object_name = 'noticiaweb_list'

class NoticiaDetailView(DetailView):
    model = NoticiaWeb
    template_name = 'noticias/noticiaweb_detail.html'