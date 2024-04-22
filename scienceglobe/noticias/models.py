from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

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
                name='genero_name_case_insensitive_unique',
                violation_error_message = "Esse genero ja existe (case insensitive match)"
            ),
        ]

class Noticia(models.Model):
    """Modelo representando um noticia."""
    title = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.RESTRICT, null=True)
    # Foreign Key usado pois um Noticia so pode ter um autor, mas um autor pode ter varios Noticias.
    # Autor como string pois ainda nao foi especificado.

    Texto = models.TextField(
        max_length=4000, help_text="Insira o texto da noticia")

    
    Genero = models.ForeignKey(
        Genero, on_delete=models.RESTRICT, help_text="Selecione o genero da noticia")
    # Foreign Key usado pois um Noticia so pode ter um Genero, mas um Genero pode ter varios Noticias.
    # Classe Genero ja foi definida entao especificamos o objeto.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('noticia-detail', args=[str(self.id)])
    
class Autor(models.Model):
    """Modelo representando um Autor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nascimento = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('autor-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'