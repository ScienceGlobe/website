from django.shortcuts import render
from .models import Artigo, Autor, Tipo

# Create your views here.

def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "artigos.html", {})