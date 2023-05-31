from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Prefetch, Case, When, Value, BooleanField, Count, Q
from utils.scrape.scrape import get_cards
from .models import Investment, InvestmentUsp, Category, Provider, Promotion

# Create your views here.
def get_investments(category, provider):
    if category == None:
        if provider == "0" or provider == None:
            number = Investment.objects.count()
            queryset = Investment.objects.prefetch_related('investment_usp').all()[:20]
        else:
            number = Investment.objects.filter(provider_id=provider).count()
            queryset = Investment.objects.prefetch_related(
                'investment_usp').filter(provider_id=provider)[:20]
    else:
        query = str(category) + ','
        if provider == "0" or provider == None:
            number = Investment.objects.filter(category__contains=query).count()
            queryset = Investment.objects.filter(
                category__contains=query).prefetch_related('investment_usp').all()[:20]
        else:
            number = Investment.objects.filter(category__contains=query).filter(
                provider_id=provider).count()
            queryset = Investment.objects.filter(category__contains=query).prefetch_related(
                'investment_usp').filter(provider_id=provider)[:20]
    return number, queryset

def investments(request, category=None):
    url = 'https://www.moneysmart.hk/en/online-brokerage'
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
    number, queryset = get_investments(category, provider)
    filters = Promotion.objects.all()

    return render(request, "pages/investments/investments.html", {"Title":"Investment", "cards": queryset, "number": number, "provider_caption":"Providers", "providers": providers, "prov": provider, "feature_caption":"Online Brokerage Features", "filter_caption":"Promotions", "filters":filters})
