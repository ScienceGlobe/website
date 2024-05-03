from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='noticias'),
    path('todas', views.NoticiasView.as_view(), name = 'todas'),
    path('noticia/<str:pk>', views.NoticiaDetailView.as_view(), name='noticia-detail'),
]