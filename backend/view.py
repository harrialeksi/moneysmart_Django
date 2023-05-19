from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def login_user(request):
    message = None
    if request.method == 'POST':
        # form = CustomLoginForm(request.POST)
        message = 'Invalid Credentials'
        return Response(message, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        message = "Login Form"
        return Response(message, status=status.HTTP_100_CONTINUE)