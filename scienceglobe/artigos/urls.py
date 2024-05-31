from django.urls import path
from . import views
from .views import filtrar_artigos_por_genero


urlpatterns = [
    path('', views.home_view, name = 'artigos'),
    path('todos', views.ArtigosView.as_view(), name = 'todos'),
    path('artigo/<str:pk>', views.ArtigoDetailView.as_view(), name='artigo-detail'),
    path('economia/', filtrar_artigos_por_genero, {'genero': 'Economia'}, name='economia'),
    path('tecnologia/', filtrar_artigos_por_genero, {'genero': 'Tecnologia'}, name='tecnologia'),
    path('meio-ambiente/', filtrar_artigos_por_genero, {'genero': 'Meio Ambiente'}, name='ambiente'),
    path('ciencias/', filtrar_artigos_por_genero, {'genero': 'Ciências'}, name='ciencias'),
]