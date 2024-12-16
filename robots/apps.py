from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = 'robots'


class RobotsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'robots'

    def ready(self):
        import robots.signals