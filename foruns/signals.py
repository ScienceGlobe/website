from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import GeneroForum

@receiver(post_migrate)
def create_default_generos(sender, **kwargs):
    if sender.name == 'foruns':
        generos = ['Duvidas', 'Tecnologia', 'Curiosidades', 'Ciências', 'Outros']
        for genero in generos:
            GeneroForum.objects.get_or_create(name=genero)
            print(f"GeneroForum ({genero}) criado com sucesso.")