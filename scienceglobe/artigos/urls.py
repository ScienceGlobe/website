from django.urls import path
from . import views
from .views import filtrar_artigos_por_genero


urlpatterns = [
    path('', views.home_view, name = 'artigos'),
    path('todos', views.ArtigosView.as_view(), name = 'todos'),
    path('artigo/<str:pk>', views.ArtigoDetailView.as_view(), name='artigo-detail'),
    path('ciências_físicas_e_engenharia/', filtrar_artigos_por_genero, {'genero': 'Ciências físicas e engenharia'}, name='ciencias-fisica'),
    path('cultura/', filtrar_artigos_por_genero, {'genero': 'Cultura'}, name='cultura'),
    path('saude/', filtrar_artigos_por_genero, {'genero': 'Saude'}, name='saude'),
    path('tecnologia/', filtrar_artigos_por_genero, {'genero': 'Tecnologia'}, name='art_tecnologia'),
]