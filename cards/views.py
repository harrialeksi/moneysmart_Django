from django.shortcuts import render
from django.db.models import Q
from utils.scrape.scrape import get_data
from .models import Card, CardUsp, Provider, Association, HeroSection


def scrape_card(url):
    cards = get_data(url)

    # Delete all rows in CardDetail, CardUsp table
    CardUsp.objects.all().delete()

    for card in cards:
        row = Card.objects.get(url=card['url'])
        row.image = card['img_src']
        row.disclosure = card['disclosure']
        row.execlusive = card['badge_execlusive']
        row.badge_label = card['badge_label']
        row.badge_primary = card['badge_primary']
        row.snippet = card['snippet']
        row.snippet_img = card['snippet_img']
        # row.url = card['url']
        row.promotion = card['promotion']
        row.keyfeatures = card['keyFeatures']
        row.annualinterest = card['annualInterest']
        row.incomeequirement = card['incomeRequirement']
        row.cardassociation = card['cardAssociation']
        row.wirelesspayment = card['wirelessPayment']
        row.save()

        for usp in card['usp']:
            car_usp = CardUsp.objects.create(
                dd=usp['ratio'], dt=usp['text'], card_id=row.id)
            car_usp.save()

def get_cards(category, provider, assoc, data_limit = 20):
    number = Card.objects
    queryset = Card.objects.prefetch_related('card_usp')

    if provider != "0" and provider != None:
        number = number.filter(provider_id=provider)
        queryset = queryset.filter(provider_id=provider)

    if category != None:
        query = ',' +str(category) + ','
        number = number.filter(category__contains=query)
        queryset = queryset.filter(category__contains=query)

    if assoc !=None:
        number = number.filter(association__contains=assoc)
        queryset = queryset.filter(association__contains=assoc)
        
    return number.count(), queryset.all()[:int(data_limit)]


def cards(request, category=None):
    provider = request.GET.get('provider')
    assoc = request.GET.get('assoc')
    data_limit = request.GET.get('end')
    if (data_limit == None): data_limit = 20
    providers = Provider.objects.all()
    filters = Association.objects.all()
    heros = HeroSection.objects.all()
    # Retrieve all cards joined with their related card details
    number, queryset = get_cards(category, provider, assoc, data_limit)

    return render(request, "pages/cards/cards.html",
                  {"Title": "Credit Cards", "Heros":heros, "MoreIndex":6, "h3":"Best Credit Cards in Hong Kong", "p":"Compare Hong Kong credit cards to earn most air miles, cashback and welcome offers, apply through Crediboo to get extra rewards! <br> Find out which credit cards suit your spending pattern the most to enjoy welcome offers, points, cash rebates, air miles, cash vouchers, gifts and many more in your daily spending. Apply for the credit card that gives you the best credit card offers!",
                   "cards": queryset, "number": number, "prov": provider, "provider_caption": "Providers", "providers": providers, "filter_caption": "Card Association", "filters": filters, "assoc": assoc, "data_end": data_limit})


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

    return render(request, "pages/cards/popular-guides_credit-cards-for-airport-lounge-access.html", {"section":"Credit Cards", "url":"../credit-cards", "broadcrump": broadcrump, "title": title, "description": desctiption,
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

    return render(request, "pages/cards/best-asia-miles-cards.html", {"section":"Credit Cards", "url":"../credit-cards", "broadcrump": broadcrump, "title": title, "description": desctiption,
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

    return render(request, "pages/cards/hotel_reward_booking.html", {"section":"Credit Cards", "url":"../credit-cards", "broadcrump": broadcrump, "title": title, "description": desctiption,
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

    return render(request, "pages/cards/expat-foreigner-hong-kong-ms.html", {"section":"Credit Cards", "url":"../credit-cards", "broadcrump": broadcrump, "title": title, "description": desctiption,
                                                                             "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "cards": queryset})


def card_detail(request, card_id):
    card = Card.objects.get(pk=card_id)
    return render(request, "pages/cards/card-detail.html", {"card": card})


def citibank(request):
    number = Card.objects.filter(provider_id=8).count()
    cards = Card.objects.filter(provider_id=8)
    providers = Provider.objects.all()
    return render(request, "pages/cards/cards.html", {"cards": cards, "providers": providers, "number": number, "prov": 8})


def standard_chartered(request):
    number = Card.objects.filter(provider_id=20).count()
    cards = Card.objects.filter(provider_id=20)
    providers = Provider.objects.all()
    return render(request, "pages/cards/cards.html", {"cards": cards, "providers": providers, "number": number, "prov": 20})


def american_express(request):
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
