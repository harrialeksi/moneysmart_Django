from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("dining", views.dining, name="dining"),
    # path("<int:category>", views.accounts, name="category"),
]