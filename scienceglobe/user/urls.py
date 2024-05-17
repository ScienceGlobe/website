from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('store/',views.store, name='store'),
    path('painel/',views.painel, name='painel'),
    path('dologin/',views.dologin, name='dologin'),
    path('profile/',views.profile, name= 'profile'),

]