from django.urls import path
from . import views
from .views import ForumPostCreate, filtrar_forumpost_por_genero

urlpatterns = [
    path('foruns/', views.ForumPostListView.as_view(), name='forumpost'),
    path('autor/<int:pk>', views.ForumListbyAuthorView.as_view(), name='forumpost-by-author'),
    path('forum/<int:pk>', views.ForumPostDetailView.as_view(), name='forumpost-detail'),
    path('autores/', views.AutorListView.as_view(), name='autores'),
    path('forum/<int:pk>/comment/', views.ForumCommentCreate.as_view(), name='forumpost_comment'),
    path('forus/novo/',  ForumPostCreate, name='forumpost-create'),
    path('forumpost/<int:pk>/like/', views.like_forum_post, name='like_forum_post'),
    path('forumpost/comment/<int:pk>/like/', views.like_forum_comment, name='like_forum_comment'),
    path('curiosidades/', filtrar_forumpost_por_genero, {'genero': 'Curiosidades'}, name='forum_curiosidades'),
    path('tecnologia/', filtrar_forumpost_por_genero, {'genero': 'Tecnologia'}, name='forum_tecnologia'),
    path('duvidas/', filtrar_forumpost_por_genero, {'genero': 'Duvidas'}, name='forum_duvidas'),
    path('ciencias/', filtrar_forumpost_por_genero, {'genero': 'Ciências'}, name='forum_ciencias'),
    path('outros/', filtrar_forumpost_por_genero, {'genero': 'Outros'}, name='forum_outros'),
]