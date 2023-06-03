"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import login_user, signup_user, verifyEmail, reset_passowrd
from .view import index

# urls = [
#     path('products/', include('base.urls.product_urls')),
#     path('users/', include('base.urls.user_urls')),
#     path('orders/', include('base.urls.order_urls')),
#     path('air/', include('base.urls.air_urls')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('signup/', signup_user, name='signup'),
    path('reset-password/', reset_passowrd, name='reset_password'),
    path('verify/<str:token>/', verifyEmail, name='verify-email'),
    path('credit-cards/', include('cards.urls')),
    path('personal-loan/', include('loans.urls')),
    path('savings-account/', include('accounts.urls')),
    path('online-brokerage/', include('investment.urls')),
    path('blog/', include('blog.urls')),
    path('rewards/', include('reward.urls')),
    path('FAQs/', include('faqs.urls')),
    # path('api/v1/', include(urls)),
]
