from django.db import models


# Create your models here.

from datetime import date
from django.db.models.functions import Lower
from django.urls import reverse
from django.contrib.auth.models import User



class AutorPost(models.Model):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Informe sua Bio")
    
    class Meta:
        ordering = ["user","bio"]

    def get_absolute_url(self):
        return reverse('forumpost-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user.username
    

class GeneroForum(models.Model):

    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Insira um genero pra posts de Forums"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('generoForum-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='generoForum_name_case_insensitive_unique',
                violation_error_message = "Esse genero ja existe (case insensitive match)"
            ),
        ]



class ForumPost(models.Model):

    name = models.CharField(max_length=200)
    genero = models.ForeignKey(GeneroForum, on_delete=models.CASCADE,null=True, help_text="Selecione o genero do seu post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=2000, help_text="Insira o texto do seu post")
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='forum_post_likes', blank=True)
    
    class Meta:
        ordering = ["-post_date"]
    
    def get_absolute_url(self):
        return reverse('forumpost-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    
    def total_likes(self):
        return self.likes.count()
        
        
class ForumPostComment(models.Model):

    description = models.TextField(max_length=1000, help_text="Insira seu comentario aqui")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    ForumPost = models.ForeignKey(ForumPost, null=True ,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='forum_comment_likes', blank=True)
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring
    
    def total_likes(self):
        return self.likes.count()