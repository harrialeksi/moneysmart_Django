from django.core.mail import send_mail
from django.conf import settings
from dotenv import load_dotenv
import os

def send_email(subject, message, to):
    send_mail(subject, message, os.getenv('DEFAULT_FROM_EMAIL'), [to])