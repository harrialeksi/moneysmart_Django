from django.core.mail import EmailMessage
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()
def send_email(subject, message, to):
    print(to)
    try:
        email = EmailMessage(subject, message, os.getenv(
            'DEFAULT_FROM_EMAIL'), [to])

        email.send()
        return True
    except:
        return False
