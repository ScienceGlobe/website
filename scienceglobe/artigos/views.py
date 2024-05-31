from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Autor, ArtigoWeb, Tipo, Genero

# Create your views here.

def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "artigos.html", {})

class ArtigosView(ListView):
    model = ArtigoWeb
    context_object_name = 'artigoweb_list'

class ArtigoDetailView(DetailView):
    model = ArtigoWeb
    template_name = 'artigos/artigoweb_detail.html'

def filtrar_artigos_por_genero(request, genero):
    
    artigos = ArtigoWeb.objects.filter(genero__name=genero)
    
    return render(request, 'artigos/artigoweb_por_genero.html', {'artigos': artigos, 'genero': genero})
