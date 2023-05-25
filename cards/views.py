from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Prefetch, Case, When, Value, BooleanField, Count
from utils.scrape.scrape import get_cards, get_card
from .models import Card, CardUsp, Provider


def cards(request):
    url = 'https://www.moneysmart.hk/en/credit-cards'
    print(request.GET.get('provider'))
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

    # Retrieve all cards joined with their related card details
    queryset = Card.objects.prefetch_related('card_usp').all()[:20]
    providers = Provider.objects.all()

    # # Serialize the data to JSON format
    # data = serializers.serialize('json', queryset)

    # # Send the JSON response
    # return HttpResponse(data, content_type='application/json')
    return render(request, "cards.html", {"cards": queryset, "providers": providers})


def card_provider(request, provider_id):
    cards = Card.objects.filter(provider_id=provider_id)
    data = serializers.serialize('json', cards)
    return HttpResponse(data, content_type='application/json')


def card_provider_association(request, provider_id, association_id):
    cards = Card.objects.filter(
        provider_id=provider_id, association_id=association_id)
    data = serializers.serialize('json', cards)
    return HttpResponse(data, content_type='application/json')


def cash_back(request):
    url = 'https://www.moneysmart.sg/credit-cards/cash-back'
    cards = get_cards(url)
    return JsonResponse(cards, safe=False)


def air_miles(request):
    url = 'https://www.moneysmart.sg/credit-cards/air-miles'
    cards = get_cards(url)
    return JsonResponse(cards, safe=False)


def petrol(request):
    url = 'https://www.moneysmart.sg/credit-cards/petrol'
    cards = get_cards(url)
    return JsonResponse(cards, safe=False)


def shopping(request):
    url = 'https://www.moneysmart.sg/credit-cards/shopping'
    cards = get_cards(url)
    return JsonResponse(cards, safe=False)
