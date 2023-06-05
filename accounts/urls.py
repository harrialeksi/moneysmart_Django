from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.accounts, name="accounts"),
    path("<int:category>", views.accounts, name="category"),
    path("time-deposit-ms", views.time_deposit_ms, name="time-deposit-ms"),

]