from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Prefetch, Case, When, Value, BooleanField, Count, Q
from utils.scrape.scrape import get_cards
from .models import Card, CardUsp, Provider


def get_cards(category, provider):
    if category == None:
        if provider == "0" or provider == None:
            number = Card.objects.count()
            queryset = Card.objects.prefetch_related('card_usp').all()[:20]
        else:
            number = Card.objects.filter(provider_id=provider).count()
            queryset = Card.objects.prefetch_related(
                'card_usp').filter(provider_id=provider)[:20]
    else:
        if category == 11:
            query = str(category)
        else:
            query = str(category) + ','
        if provider == "0" or provider == None:
            number = Card.objects.filter(category__contains=query).count()
            queryset = Card.objects.filter(
                category__contains=query).prefetch_related('card_usp').all()[:20]
        else:
            number = Card.objects.filter(category__contains=query).filter(
                provider_id=provider).count()
            queryset = Card.objects.filter(category__contains=query).prefetch_related(
                'card_usp').filter(provider_id=provider)[:20]
    return number, queryset


def cards(request, category=None):
    url = 'https://www.moneysmart.hk/en/credit-cards'
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
    number, queryset = get_cards(category, provider)

    return render(request, "pages/cards/cards.html", {"cards": queryset, "providers": providers, "number": number, 'prov': provider})


def airport_lounge_access(request):
    title = "Best Credit Cards for Airport Lounges in Hong Kong"
    desctiption = "High income is not necessarily a prerequisite for free access to airport lounges. Eligible cardholders can enjoy complimentary access with friends and families. Choose the ones that suit you the most."
    subtitle = "Which cards should be used for airport lounge visits?"
    sub_desc = "Click the cards below to learn more:"
    categories = [{"link": "plaza-premium", "category": "Plaza Premium Lounges",
                   "desc": "Citi PremierMiles, Citi Prestige, Citi Rewards Card, AMEX Explorer Card"},
                  {"link": "centurion-lounge", "category": "Centurion Lounge ",
                   "desc": "American Express® Platinum Credit Card"},
                  {"link": "marriott_hotels", "category": 'LoungeKey ("MCAE")',
                   "desc": "Citi Prestige Card"}]
    broadcrump = "Best Credit Cards for Airport Lounges in Hong Kong 2023"
    # Retrieve all cards joined with their related card details
    queryset = Card.objects.prefetch_related('card_usp').filter(Q(title="Citi Prestige Card") | Q(title="Citi Rewards MasterCard") | Q(
        title="American Express Explorer® Credit Card") | Q(title="The Platinum Card") | Q(title="Citi Prestige Card"))

    return render(request, "pages/cards/popular-guides_credit-cards-for-airport-lounge-access.html", {"broadcrump": broadcrump, "title": title, "description": desctiption,
                                                                                                "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "cards": queryset})


def best_asia_miles(request):
    title = "Best Asia Miles Cards in Hong Kong (Updated in Oct 2022)"
    desctiption = "High income is not necessarily a prerequisite for free access to airport lounges. Eligible cardholders can enjoy complimentary access with friends and families. Choose the ones that suit you the most."
    subtitle = "Which cards should be used for airport lounge visits?"
    sub_desc = "Click the cards below to learn more:"
    categories = [{"link": "plaza-premium-lounges", "category": "Plaza Premium Lounges",
                   "desc": "Citi PremierMiles, Citi Prestige, Citi Rewards Card, AMEX Explorer Card"},
                  {"link": "centurion-lounge", "category": "Centurion Lounge ",
                   "desc": "American Express® Platinum Credit Card"},
                  {"link": "marriott_hotels", "category": 'LoungeKey ("MCAE")',
                   "desc": "Citi Prestige Card"}]
    broadcrump = "Best Credit Cards for Airport Lounges in Hong Kong 2023"
    # Retrieve all cards joined with their related card details
    queryset = Card.objects.prefetch_related('card_usp').filter(Q(title="Citi Prestige Card") | Q(title="Citi Rewards MasterCard") | Q(
        title="American Express Explorer® Credit Card") | Q(title="The Platinum Card") | Q(title="Citi Prestige Card"))

    return render(request, "pages/cards/best-asia-miles-cards.html", {"broadcrump": broadcrump, "title": title, "description": desctiption,
                                                                                                "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "cards": queryset})


def hotel_reward_booking(request):

    title = "Best Credit Cards in Hong Kong for Hotel Promotions & Rewards 2022"
    desctiption = "There is a wide range of credit cards in the market offering hotel rewards and booking discounts. You can compare their offers and apply the ones that suit your spending pattern."
    subtitle = "Which Hotel Credit Card is Best for You?"
    sub_desc = "Learn more about credit cards that are great for the following hotel rewards programs and booking portals"
    categories = [{"link": "platinum-card", "category": "Hilton Hotels",
                   "desc": "The Platinum Card"},
                  {"link": "intercontinental_hotels", "category": "InterContinental Hotels Group (IHG) ",
                   "desc": "Citi PremierMiles Card"},
                  {"link": "marriott_hotels", "category": "Marriott Hotels",
                   "desc": "American Express Platinum Credit Card"},
                  {"link": "citibank_credit_cards", "category": "Expedia.com.hk",
                   "desc": "Citibank Credit Cards"}]
    broadcrump = "Best Credit Cards in Hong Kong for Hotel Rewards and Booking Discounts 2022"
    # Retrieve all cards joined with their related card details
    queryset = Card.objects.prefetch_related('card_usp').filter(Q(title="The Platinum Card") | Q(
        title="Citi PremierMiles Card") | Q(title="American Express® Platinum Credit Card") | Q(title="Citi Cash Back Card"))

    return render(request, "pages/cards/hotel_reward_booking.html", {"broadcrump": broadcrump, "title": title, "description": desctiption,
                                                               "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "cards": queryset})


def expat_foreigner_hong_kong_ms(request):

    title = "Best Credit Cards for Expats and Foreigners in Hong Kong"
    desctiption = "With selected credit cards, you can enjoy rewards for local and overseas spending. We have put together a list of selected credit cards. Choose the ones that match your spending pattern the most."
    subtitle = "Which cards should expats and foreigners apply?"
    sub_desc = "Click the cards below to learn more:"
    categories = [{"link": "for_cashbak", "category": "For Cashback",
                   "desc": "Standard Chartered, Citi cards"},
                  {"link": "for_airmiles", "category": "For Air Miles ",
                   "desc": "DBS, Citi, Standard Chartered cards"},
                  {"link": "for_grocery", "category": "For Grocery Shopping",
                   "desc": "Hang Seng, DBS, Citi cards "}]
    broadcrump = "Best Credit Cards for Expats and Foreigners in Hong Kong"
    # Retrieve all cards joined with their related card details
    queryset = Card.objects.prefetch_related('card_usp').filter(Q(title="Citi Cash Back Card") | Q(title="Standard Chartered Smart Card") | Q(title="DBS Black World Mastercard") | Q(title="Standard Chartered Cathay Mastercard") | Q(
        title="Citi Prestige Card") | Q(title="Hang Seng enJoy Card") | Q(title="Citi Rewards MasterCard"))

    return render(request, "pages/cards/expat-foreigner-hong-kong-ms.html", {"broadcrump": broadcrump, "title": title, "description": desctiption,
                                                                       "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "cards": queryset})


def citibank(request):
    number = Card.objects.filter(provider_id=8).count()
    cards = Card.objects.filter(provider_id=8)
    providers = Provider.objects.all()
    return render(request, "pages/cards/cards.html", {"cards": cards, "providers": providers, "number": number, "prov": 8})


def standard_chartered(request):
    number = Card.objects.filter(provider_id=20).count()
    cards = Card.objects.filter(provider_id=20)
    providers = Provider.objects.all()
    return render(request, "pages/cards/cards.html", {"cards": cards, "providers": providers, "number": number,"prov": 20})


def american_express(request):  # ===========================================
    number = Card.objects.filter(provider_id=3).count()
    cards = Card.objects.filter(provider_id=3)
    providers = Provider.objects.all()
    return render(request, "pages/cards/cards.html", {"cards": cards, "providers": providers, "number": number, "prov": 3})


def wewa_unionpay(request):  # ================================================
    number = Card.objects.filter(provider_id=8).count()
    cards = Card.objects.filter(provider_id=8)
    providers = Provider.objects.all()
    return render(request, "pages/cards/cards.html", {"cards": cards, "providers": providers, "number": number, "prov": 3})


# ==========================================
def earnmore_unionpay_card(request):
    number = Card.objects.filter(provider_id=8).count()
    cards = Card.objects.filter(provider_id=8)
    providers = Provider.objects.all()
    return render(request, "pages/cards/cards.html", {"cards": cards, "providers": providers, "number": number})
