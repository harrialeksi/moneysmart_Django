from django.urls import path

from . import views

app_name = "cards"
urlpatterns = [
    path("", views.cards, name="cards"),
    path("cash-back", views.cash_back, name="cash_back"),
    path("air-miles", views.air_miles, name="air_miles"),
    path("overseas_spending", views.overseas_spending, name="overseas_spending"),
    path("welcome-offer", views.welcome_offer, name="welcome_offer"),
    path("shopping_credit_card", views.shopping_credit_card, name="shopping_credit_card"),
    path("annual-fee-waiver", views.annual_fee_waiver, name="annual_fee_waiver"),
    path("unionpay", views.unionpay, name="unionpay"),
    path("student", views.student, name="student"),
    path("digital-wallets", views.digital_wallets, name="digital_wallets"),
    path("octopus_card_aavs", views.octopus_card_aavs, name="octopus_card_aavs"),
    path("bill_payment_credit_card", views.business_card, name="bill_payment_credit_card"),
    
    path("airport-lounge-free-access-ms", views.airport_lounge_access, name="airport_lounge_access"),
    path("hotel_reward_booking", views.hotel_reward_booking, name="hotel_reward_booking"),
    path("expat-foreigner-hong-kong-ms", views.expat_foreigner_hong_kong_ms, name="expat_foreigner_hong_kong_ms"),
    path("citibank", views.citibank, name="citibank"),
    path("standard-chartered", views.standard_chartered, name="standard_chartered"),
    path("american-express", views.american_express, name="american_express"),
    path("wewa-unionpay", views.wewa_unionpay, name="wewa_unionpay"),
    path("earnmore-unionpay-card", views.earnmore_unionpay_card, name="earnmore_unionpay_card"),
    path("<int:provider_id>/", views.card_provider, name="provider"),
    path("<int:provider_id>/<int:association_id>", views.card_provider_association, name="association"),
    # path("cash-back/", views.cash_back, name="cashback"),
    # path("air-miles/", views.air_miles, name="airmiles"),
    # path("petrol/", views.air_miles, name="pertol"),
    # path("shopping/", views.air_miles, name="shopping"),
    # path("air-mile/", views.airmile, name="airmile"),
    # path("online-shopping/", views.onlineshopping, name="onlineshopping"),
]