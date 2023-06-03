from django.shortcuts import render

# Create your views here.
def reward(request):

    return render(request, "pages/reward/latest-reward-deals.html", {"Title":"Rewards"})
