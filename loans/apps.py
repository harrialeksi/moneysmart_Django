from django.apps import AppConfig
import threading

class LoansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loans'

    def ready(self):
        # Connect the `my_startup_code` function to the `ready` signal
        from .tasks import task
        # Code to execute when app is ready
        t = threading.Thread(target=task)
        t.start()
