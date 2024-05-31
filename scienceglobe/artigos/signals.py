from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Genero

@receiver(post_migrate)
def create_default_generos(sender, **kwargs):
    if sender.name == 'artigos':
        generos = ['Ciências físicas e engenharia', 'Cultura', 'Saude', 'Tecnologia']
        for genero in generos:
            Genero.objects.get_or_create(name=genero)