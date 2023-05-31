from django.urls import path

from . import views

app_name = "investment"
urlpatterns = [
    path("", views.investments, name="investments"),
    path("<int:category>", views.investments, name="category"),
]