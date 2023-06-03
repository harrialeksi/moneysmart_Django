from django.urls import path

from . import views

app_name = "rewards"
urlpatterns = [
    path("Latest-Reward-Deals", views.reward, name="lastestReward"),
    path("Claim-Rewards", views.reward, name="claimReward"),
    path("Claim-Status", views.reward, name="claimsStatus"),
    # path("<int:category>", views.accounts, name="category"),
]