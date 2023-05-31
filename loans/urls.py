from django.urls import path

from . import views

app_name = "loans"
urlpatterns = [
    path("", views.loans, name="loans"),
    path("<int:category>", views.loans, name="category"),
    path("airport-lounge-free-access-ms", views.airport_lounge_access, name="airport_lounge_access"),
    path("hotel_reward_booking", views.hotel_reward_booking, name="hotel_reward_booking"),
    path("expat-foreigner-hong-kong-ms", views.expat_foreigner_hong_kong_ms, name="expat_foreigner_hong_kong_ms"),
    # path("cash-back/", views.cash_back, name="cashback"),
    # path("air-miles/", views.air_miles, name="airmiles"),
    # path("petrol/", views.air_miles, name="pertol"),
    # path("shopping/", views.air_miles, name="shopping"),
    # path("air-mile/", views.airmile, name="airmile"),
    # path("online-shopping/", views.onlineshopping, name="onlineshopping"),
]