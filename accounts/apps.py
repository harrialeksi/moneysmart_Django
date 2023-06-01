from django.apps import AppConfig
import threading

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # def ready(self):
    #     # Connect the `my_startup_code` function to the `ready` signal
    #     from .tasks import task
    #     # Code to execute when app is ready
    #     t = threading.Thread(target=task)
    #     t.start()
