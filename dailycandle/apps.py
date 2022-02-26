from django.apps import AppConfig


class DailycandleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dailycandle'
    
    def ready(self):
        print("Starting Scheduler ... ")
        from .stock_scheduler import stock_updater
        stock_updater.start()
