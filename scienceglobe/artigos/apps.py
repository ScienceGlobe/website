from django.apps import AppConfig


class ArtigosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artigos'
    def ready(self):
        print("Ready function is called.")
        from . import signals
        from . import updater
        updater.start()
