from django.apps import AppConfig


class ForunsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foruns'
    def ready(self):
        print("Apps de foruns inicializado.")
        from . import signals
