from django.urls import path

from . import views

app_name = "cards"
urlpatterns = [
    path("", views.cards, name="cards"),
    path("<int:category>", views.cards, name="category"),
    path("airport-lounge-free-access-ms", views.airport_lounge_access, name="airport_lounge_access"),
    path("best-asia-miles", views.best_asia_miles, name="best_asia_miles"),    
    path("hotel_reward_booking", views.hotel_reward_booking, name="hotel_reward_booking"),
    path("expat-foreigner-hong-kong-ms", views.expat_foreigner_hong_kong_ms, name="expat_foreigner_hong_kong_ms"),
    path("citibank", views.citibank, name="citibank"),
    path("standard-chartered", views.standard_chartered, name="standard_chartered"),
    path("american-express", views.american_express, name="american_express"),
    path("wewa-unionpay", views.wewa_unionpay, name="wewa_unionpay"),
    path("earnmore-unionpay-card", views.earnmore_unionpay_card, name="earnmore_unionpay_card"),
]