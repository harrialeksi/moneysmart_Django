from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from dotenv import load_dotenv
import os
from django.contrib.auth import (
    authenticate, get_user_model, login, logout
)
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from utils.email import send_email

APP_NAME = os.getenv('APP_NAME')
APP_DOMAIN = os.getenv("APP_DOMAIN")

# Create your views here.


@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == "POST":
        data = request.data
        try:
            user = authenticate(
                request, username=data['email'], password=data['password']
            )
            if user:
                if not user.is_active:
                    # ==========================================
                    return ('users:active_email')
                else:
                    login(request, user)
                    # ================================
                    return redirect('users:avtivate_email')
            else:
                message = {'detail': 'Invalid Credentials'}
                return Response(message, status=status.HTTP_406_NOT_ACCEPTABLE)
        except KeyError:
            message = {'detail': 'Field not completed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {'detail': 'Error'}
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        message = {'detail': 'Login'}
        return Response(message, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def register_user(request):
    if request.method == "POST":
        data = request.data
        try:
            user = User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password']),
                is_active=False,
            )

            # create token
            token = RefreshToken.for_user(user).access_token
            subject = f"{APP_NAME} Activation email"
            body = f"Hi {user.username} welcome to {APP_NAME}.\n Please use below link for active your account! \n\n" \
                f"{APP_DOMAIN}/api/v1/users/verify/{str(token)}/"

            send_email(subject, body, user.email)
            message = {'detail': 'Email sent'}
            return Response(message, status=status.HTTP_200_OK)
        except KeyError:
            message = {'detail': 'Invalid field'}
            return Response(message, status=status.HTTP_200_OK)
        # except:
        #     message = {'detail': 'Invalid Credentials'}
        #     return Response(message, status=status.HTTP_200_OK)
    else:
        message = {'detail': 'Register'}
        return Response(message, status=status.HTTP_200_OK)
