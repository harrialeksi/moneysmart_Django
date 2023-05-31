from django.urls import path

from . import views

app_name = "loans"
urlpatterns = [
    path("", views.loans, name="loans"),
    path("<int:category>", views.loans, name="category"),
]