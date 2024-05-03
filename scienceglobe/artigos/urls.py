from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = 'artigos'),
    path('todos', views.ArtigosView.as_view(), name = 'todos'),
    path('artigo/<str:pk>', views.ArtigoDetailView.as_view(), name='artigo-detail'),
]