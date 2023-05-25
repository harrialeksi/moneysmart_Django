from django.urls import path

from . import views

app_name = "cards"
urlpatterns = [
    path("", views.cards, name="cards"),
    path("<int:provider_id>/", views.card_provider, name="provider"),
    path("<int:provider_id>/<int:association_id>", views.card_provider_association, name="association"),
    # path("cash-back/", views.cash_back, name="cashback"),
    # path("air-miles/", views.air_miles, name="airmiles"),
    # path("petrol/", views.air_miles, name="pertol"),
    # path("shopping/", views.air_miles, name="shopping"),
    # path("air-mile/", views.airmile, name="airmile"),
    # path("online-shopping/", views.onlineshopping, name="onlineshopping"),
]