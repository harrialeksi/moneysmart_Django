from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Prefetch, Case, When, Value, BooleanField, Count, Q
from utils.scrape.scrape import get_cards
from .models import Account, AccountUsp, Category, Provider

# Create your views here.
def get_accounts(category, provider):
    if category == None:
        if provider == "0" or provider == None:
            number = Account.objects.count()
            queryset = Account.objects.prefetch_related('account_usp').all()[:20]
        else:
            number = Account.objects.filter(provider_id=provider).count()
            queryset = Account.objects.prefetch_related(
                'account_usp').filter(provider_id=provider)[:20]
    else:
        query = str(category) + ','
        if provider == "0" or provider == None:
            number = Account.objects.filter(category__contains=query).count()
            queryset = Account.objects.filter(
                category__contains=query).prefetch_related('account_usp').all()[:20]
        else:
            number = Account.objects.filter(category__contains=query).filter(
                provider_id=provider).count()
            queryset = Account.objects.filter(category__contains=query).prefetch_related(
                'account_usp').filter(provider_id=provider)[:20]
    return number, queryset

def accounts(request, category=None):
    url = 'https://www.moneysmart.hk/en/savings-account'
    provider = request.GET.get('provider')
    # cards = get_cards(url)

    # # Delete all rows in CardDetail, CardUsp table
    # CardUsp.objects.all().delete()

    # for card in cards:
    #     row = Card.objects.get(title=card['title'])
    #     row.image = card['img_src']
    #     row.disclosure = card['disclosure']
    #     row.execlusive = card['badge_execlusive']
    #     row.badge_label = card['badge_label']
    #     row.badge_primary = card['badge_primary']
    #     row.snippet = card['snippet']
    #     row.snippet_img = card['snippet_img']
    #     row.promotion = card['promotion']
    #     row.keyfeatures = card['keyFeatures']
    #     row.annualinterest = card['annualInterest']
    #     row.incomeequirement = card['incomeRequirement']
    #     row.cardassociation = card['cardAssociation']
    #     row.wirelesspayment = card['wirelessPayment']
    #     row.save()

    # for usp in card['usp']:
    #     car_usp = CardUsp.objects.create(dd=usp['ratio'], dt=usp['text'], card_id=row.id)
    #     car_usp.save()

    providers = Provider.objects.all()

    # Retrieve all cards joined with their related card details
    number, queryset = get_accounts(category, provider)

    return render(request, "pages/accounts/accounts.html", {"cards": queryset, "number": number, "provider_caption":"Providers", "providers": providers, "prov": provider})
