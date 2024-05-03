from django.db import models


# Create your models here.

from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User



class AutorPost(models.Model):
    """Modelo representando um autor de um post"""
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Informe sua Bio")
    
    class Meta:
        ordering = ["user","bio"]

    def get_absolute_url(self):
        return reverse('forum_list_by_author', args=[str(self.id)])

    def __str__(self):
        return self.user.username


class ForumPost(models.Model):
    """Modelo representando um Post no Forum."""
    name = models.CharField(max_length=200)
    author = models.ForeignKey(AutorPost, on_delete=models.SET_NULL, null=True)
      # Foreign Key usado pois um post no forum pode ter apenas um autor, mas usuarios podem ter varios posts no Forum.
    description = models.TextField(max_length=2000, help_text="Insira o texto do seu post")
    post_date = models.DateField(default=date.today)
    
    class Meta:
        ordering = ["-post_date"]
    
    def get_absolute_url(self):
        return reverse('forumpost-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
        
        
class ForumPostComment(models.Model):
    """
    Modelo representando um comentario em um post no forum.
    """
    description = models.TextField(max_length=1000, help_text="Insira seu comentario aqui")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because ForumPostComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    ForumPost= models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring