from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticia

# Create your views here.

def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "noticias.html", {})

class NoticiasView(ListView):
    model = Noticia
    context_object_name = 'noticia_list'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticias/noticia_detail.html'