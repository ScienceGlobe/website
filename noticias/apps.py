from django.apps import AppConfig


class NoticiasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'noticias'
    def ready(self):
        print("Ready function is called.")
        from . import signals
        from . import updater
        updater.start()


