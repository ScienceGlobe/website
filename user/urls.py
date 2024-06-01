from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('create/', views.create, name='create'),
    path('store/',views.store, name='store'),
    path('painel/',views.painel, name='painel'),
    path('dologin/',views.dologin, name='dologin'),
    path('profile/',views.profile, name= 'profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
