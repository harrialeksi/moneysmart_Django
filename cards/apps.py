from django.apps import AppConfig
import threading
from .tasks import task

class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'

    # def ready(self):
    #     # Code to execute when app is ready
    #     t = threading.Thread(target=task)
    #     t.start()
