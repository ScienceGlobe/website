from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Genero

@receiver(post_migrate)
def create_default_generos(sender, **kwargs):
    if sender.name == 'artigos':
        generos = ['Economia', 'Tecnologia', 'Meio Ambiente', 'Ciências']
        for genero in generos:
            Genero.objects.get_or_create(name=genero)