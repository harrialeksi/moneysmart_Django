from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from dotenv import load_dotenv
import os
from django.contrib.auth import (
    authenticate, get_user_model, login, logout
)
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
import jwt
from utils.email import send_email

load_dotenv()
APP_NAME = os.getenv('APP_NAME')
APP_DOMAIN = os.getenv("APP_DOMAIN")
SECRET_KEY = os.getenv("SECRET_KEY")

# Create your views here.

#Login handler
#made by @superbaby81230
#date: 19/5/2023
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
        return render(request, "login.html")

#Register handler
#made by @superbaby81230
#date: 19/5/2023
@api_view(['POST', 'GET'])
def signup_user(request):
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

            result = send_email(subject, body, user.email)
            if result:
                message = {
                    'detail': f'Welcome to {APP_NAME}. You should verify your email.Please check your Inbox. We sent an email.',
                }
                return Response(message, status=status.HTTP_201_CREATED)
            else:
                message = {
                    'detail': 'There\'s a problem on sending email.',
                    'token': f"{APP_DOMAIN}/api/v1/users/verify/{str(token)}/"
                }
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except KeyError:
            message = {'detail': 'Invalid field'}
            return Response(message, status=status.HTTP_200_OK)
        # except:
        #     # user = User.objects.get(username=data['email'])

        #     # # update the user's password
        #     # user.password = make_password(data['password'])
        #     # user.save()

        #     # if user and not user.is_active:

        #     #     # create token
        #     #     token = RefreshToken.for_user(user).access_token

        #     #     # send activation email to user
        #     #     subject = f"{APP_NAME} Activation email"
        #     #     body = f"Hi {user.username} welcome back to {APP_NAME}.\n Please use below link for active your account! \n\n" \
        #     #         f"{APP_DOMAIN}/api/v1/users/verify/{str(token)}/"
                
        #     #     result = send_email(subject, body, user.email)

        #     #     if result:
        #     #         message = {
        #     #             'detail': 'User with this email already exists but is not active. You should verify your email.Please check your Inbox. We sent an email.Using new password'
        #     #         }
        #     #         return Response(message, status=status.HTTP_400_BAD_REQUEST)
        #     #     else:
        #     #         message = {
        #     #             'detail': 'There\'s a problem on sending email.',
        #     #             'token': f"{APP_DOMAIN}/api/v1/users/verify/{str(token)}/"
        #     #         }
        #     #         return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #     # elif user and user.is_active:
        #         message = {
        #             'detail': 'Failed to register'
        #         }
        #         return Response(message, status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request, "signup.html")

#Verify email handler
#made by @superbaby81230
#date: 19/5/2023
@api_view(['GET'])
def verifyEmail(request, token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, ['HS256'])
        user = User.objects.get(id=payload['user_id'])
        user.is_active = 1
        user.save()
        return redirect(f'{APP_DOMAIN}/login?token=success')
    except:
        return redirect(f'{APP_DOMAIN}/login?token=fail')