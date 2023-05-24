from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Prefetch, Case, When, Value, BooleanField, Count
from utils.scrape.scrape import get_cards
from .models import Card, CardDetail, CardUsp


def best(request):
    url = 'https://www.moneysmart.hk/en/credit-cards'
    # cards = get_cards(url)

    # # Delete all rows in CardDetail, CardUsp table
    # CardDetail.objects.all().delete()
    # CardUsp.objects.all().delete()

    # for card in cards:
    #     row = Card.objects.get(title=card['title'])
    #     row.image = card['img_src']
    #     row.save()

    #     cardDetail = CardDetail.objects.create(disclosure=card['disclosure'], execlusive=card['badge_execlusive'], badge_label=card['badge_label'],
    #                                            badge_primary=card['badge_primary'], snippet=card['snippet'], snippet_img=card['snippet_img'], card_id=row.id)
    #     cardDetail.save()

    #     for usp in card['usp']:
    #         car_usp = CardUsp.objects.create(dd=usp['ratio'], dt=usp['text'], card_id=row.id)
    #         car_usp.save()

    # Retrieve all cards joined with their related card details
    queryset = Card.objects.all().prefetch_related('card_details').prefetch_related('card_usp')

    # Serialize the data to JSON format
    data = serializers.serialize('json', queryset)

    # Send the JSON response
    return HttpResponse(data, content_type='application/json')


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
