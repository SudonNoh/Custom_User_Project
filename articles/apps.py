from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
    verbose_name = 'Articles'
    
    def ready(self):
        import articles.api.signals

default_app_config = 'articles.api.ArticlesConfig'
        