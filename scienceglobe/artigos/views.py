from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Artigo, Autor, Tipo

# Create your views here.

def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "artigos.html", {})

class ArtigosView(ListView):
    model = Artigo
    context_object_name = 'artigo_list'

class ArtigoDetailView(DetailView):
    model = Artigo
    template_name = 'artigos/artigo_detail.html'
