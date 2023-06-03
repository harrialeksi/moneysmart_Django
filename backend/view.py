from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'index.html', {"Title":"Home"})

def contact(request):
    return render(request, 'pages/contact/contact-us.html', {"Title":"Contact"})