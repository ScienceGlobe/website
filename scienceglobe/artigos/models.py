from django.db import models

from django.db import models
from django.urls import reverse

from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class Tipo(models.Model):
    """Modelo representando um tipo de artigo"""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Insira um tipo de artigo"
    )

    def __str__(self):
        """String pra representar o objeto do Modelo"""
        return self.name

    def get_absolute_url(self):
        """Retorna uma url pra acessar uma instancia de tipo"""
        return reverse('tipo-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='tipo_name_case_insensitive_unique',
                violation_error_message = "Esse tipo ja existe (case insensitive match)"
            ),
        ]

class Genero(models.Model):
    """Modelo representando um genero de noticia"""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Insira um genero de noticia"
    )

    def __str__(self):
        """String pra representar o objeto do Modelo"""
        return self.name

    def get_absolute_url(self):
        """Retorna uma url pra acessar uma instancia de Genero"""
        return reverse('genero-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genero_artigo_name_case_insensitive_unique',
                violation_error_message = "Esse genero ja existe (case insensitive match)"
            ),
        ]

class Artigo(models.Model):
    """Modelo representando um artigo."""
    title = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.RESTRICT, null=True)
    # Foreign Key usado pois um artigo so pode ter um autor, mas um autor pode ter varios artigos.
    # Autor como string pois ainda nao foi especificado.

    texto = models.TextField(
        max_length=4000, help_text="Insira o texto do artigo")

    
    tipo = models.ForeignKey(
        Tipo, on_delete=models.RESTRICT, help_text="Selecione o tipo do artigo")
    # Foreign Key usado pois um artigo so pode ter um tipo, mas um tipo pode ter varios artigos.
    # Classe Tipo ja foi definida entao especificamos o objeto.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('artigo-detail', args=[str(self.id)])
    
class Autor(models.Model):
    """Modelo representando um Autor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('autor-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
class ArtigoWeb(models.Model):

    title = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.RESTRICT, null=True)
    corpo = models.TextField(max_length=5000)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('artigo-detail', args=[str(self.id)])