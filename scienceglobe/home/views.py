from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})