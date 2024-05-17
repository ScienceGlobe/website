from django.urls import path
from . import views
from .views import filtrar_noticias_por_genero

urlpatterns = [
    path('', views.home_view, name='noticias'),
    path('todas', views.NoticiasView.as_view(), name = 'todas'),
    path('noticia/<str:pk>', views.NoticiaDetailView.as_view(), name='noticiaweb-detail'),
    path('economia/', filtrar_noticias_por_genero, {'genero': 'Economia'}, name='economia'),
    path('tecnologia/', filtrar_noticias_por_genero, {'genero': 'Tecnologia'}, name='tecnologia'),
    path('meio-ambiente/', filtrar_noticias_por_genero, {'genero': 'Meio Ambiente'}, name='ambiente'),
    path('ciencias/', filtrar_noticias_por_genero, {'genero': 'Ciências'}, name='ciencias'),
]