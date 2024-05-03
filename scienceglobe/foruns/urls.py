from django.urls import path
from . import views

urlpatterns = [
    path('foruns/', views.ForumPostListView.as_view(), name='forumpost'),
    path('autor/<int:pk>', views.ForumListbyAuthorView.as_view(), name='forumpost-by-author'),
    path('forum/<int:pk>', views.ForumPostDetailView.as_view(), name='forumpost-detail'),
    path('autores/', views.AutorListView.as_view(), name='autores'),
    path('forum/<int:pk>/comment/', views.ForumCommentCreate.as_view(), name='forumpost_comment'),

]