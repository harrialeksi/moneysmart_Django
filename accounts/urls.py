from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.accounts, name="accounts"),
    path("<int:category>", views.accounts, name="category"),
]