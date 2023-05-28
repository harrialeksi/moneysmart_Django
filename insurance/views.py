from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Prefetch, Case, When, Value, BooleanField, Count, Q
from utils.scrape.scrape import get_cards
from .models import Insurance, InsuranceUsp, Insurer


def insurances(request):
    url = 'https://www.moneysmart.hk/en/travel-insurance'
    insurances = get_cards(url)

    # Delete all rows in CardDetail, CardUsp table
    InsuranceUsp.objects.all().delete()

    for insurance in insurances:
        row = Insurance.objects.get(title=insurance['title'])
        row.image = insurance['img_src']
        row.disclosure = insurance['disclosure']
        row.execlusive = insurance['badge_execlusive']
        row.badge_label = insurance['badge_label']
        row.badge_primary = insurance['badge_primary']
        row.snippet = insurance['snippet']
        row.snippet_img = insurance['snippet_img']
        row.promotions = insurance['promotion']
        row.keyfeatures = insurance['keyFeatures']
        row.travel_incon = insurance['travel_inconvenience']
        row.save()

        for usp in insurance['usp']:
            insurance_usp = InsuranceUsp.objects.create(
                dd=usp['ratio'], dt=usp['text'], insurance_id=row.id)
            insurance_usp.save()

    # Retrieve all cards joined with their related card details
    number = Insurance.objects.count()
    queryset = Insurance.objects.prefetch_related('insurance_usp').all()[:20]
    insures = Insurer.objects.all()

    return render(request, "cards.html", {"cards": queryset, "providers": insures, "number": number})


def best_covid_19(request):
    title = "Best COVID-19 Travel Insurance in HK 2023"
    desctiption = "With the spread of Omicron, your travel plans may well be disrupted. Wondering what travel insurance in Hong Kong covers COVID 19-related issues? To save you from doing your own research, MoneySmart has put together a quick overview relating to travel insurance that offer COVID 19 coverage for you."
    subtitle = "COVID-19 Travel Insurance Guide"
    sub_desc = "Click the buttons below to jump to the sections you want to learn more about:"
    categories = [{"link": "covid-19-travel-insurance-providers'-latest-updates", "category": "COVID-19 Travel Insurance 101",
                   "desc": "COVID-19 Travel Insurance Providers"},
                  {"link": "things-to-note-about-covid-19-travel-insurance", "category": "COVID-19 Travel Insurance 101",
                   "desc": "Things to Note about COVID 19 Travel Insurance"},
                  {"link": "does-travel-insurance-cover-quarantine", "category": 'Quarantine',
                   "desc": "Does COVID 19 Travel Insurance Cover Quarantine?"},
                  {"link": "faq", "category": 'COVID-19 Travel Insurance 101',
                   "desc": "FAQ"}]
    broadcrump = "Best COVID-19 Travel Insurance Hong Kong 2023"
    broad_url = '{% url "insurance: coronavirus" %}'
    image_url = ''
    # Retrieve all cards joined with their related card details
    queryset = Insurance.objects.prefetch_related('insurance_usp').filter(Q(title="AXA SmartTraveller Plus Economy Plan (Single Journey)") | Q(title="Allianz Travel - Gold Plan [for ages 2 to 54]") | Q(
        title="Avo Travel Protection (Upgraded) - Lite (Area 1)"))

    return render(request, "pages/coronavirus.html", {"broadcrump": broadcrump, "title": title, "description": desctiption, 'image_url': image_url,
                                                                                                "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "cards": queryset})


def flight_delay(request):

    title = "Best Travel Insurance for Flight Delays and Cancellations"
    desctiption = "Travel insurance has become more important than ever under the pandemic, as travellers need to be prepared for any sudden events. Flight delays and cancellation have become more common, as seen in HK Express and Cathay Pacific cancelling over 100 flights between Hong Kong and Japan in February 2023 due to Japan government's flight restrictions. What are the best Travel Insurance for flight delays and cancellations? Which travel insurance offer Covid-19 coverage? MoneySmart has got you covered!"
    subtitle = "Which travel insurance is the best for flight delays and cancellations coverage?"
    sub_desc = "Click the plans below to find out:"
    categories = [{"link": "high-flight-delay-protection", "category": "",
                   "desc": "High flight delay protection"},
                  {"link": "high-trip-cancellation-protection", "category": "",
                   "desc": "High trip cancellation protection"}]
    broadcrump = "Best Travel Insurance for Flight Delays and Cancellations"
    image_url = ''
    # Retrieve all cards joined with their related card details
    queryset = Insurance.objects.prefetch_related('insurance_usp').filter(Q(title="AXA SmartTraveller Plus Economy Plan (Single Journey)") | Q(title="Allianz Travel - Silver Plan [for ages 2 to 54]") | Q(
        title="BOCG Insurance Universal Voyage Travel Insurance Silver Plan (Worldwide)") | Q(title="Generali Bravo Travel Protector (Classic Plan)") | Q(title="AXA SmartTraveller Plus Economy Plan (Single Journey)") | Q(title="BOCG Insurance Universal Voyage Travel Insurance Silver Plan (Worldwide)"))

    return render(request, "pages/insurances/flight_delay.html", {"broadcrump": broadcrump, "title": title, "description": desctiption, 'image_url': image_url,
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

    return render(request, "pages/expat-foreigner-hong-kong-ms.html", {"broadcrump": broadcrump, "title": title, "description": desctiption,
                                                                       "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "cards": queryset})


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
    number = Card.objects.filter(category__contains='1,').count()
    cards = Card.objects.filter(category__contains='1,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def air_miles(request):
    number = Card.objects.filter(category__contains='2,').count()
    cards = Card.objects.filter(category__contains='2,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def overseas_spending(request):
    number = Card.objects.filter(category__contains='3,').count()
    cards = Card.objects.filter(category__contains='3,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def welcome_offer(request):
    number = Card.objects.filter(category__contains='4,').count()
    cards = Card.objects.filter(category__contains='4,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def shopping_credit_card(request):
    number = Card.objects.filter(category__contains='5,').count()
    cards = Card.objects.filter(category__contains='5,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def annual_fee_waiver(request):
    number = Card.objects.filter(category__contains='6,').count()
    cards = Card.objects.filter(category__contains='6,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def unionpay(request):
    number = Card.objects.filter(category__contains='7,').count()
    cards = Card.objects.filter(category__contains='7,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def student(request):
    number = Card.objects.filter(category__contains='8,').count()
    cards = Card.objects.filter(category__contains='8,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def digital_wallets(request):
    number = Card.objects.filter(category__contains='9,').count()
    cards = Card.objects.filter(category__contains='9,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def business_card(request):
    number = Card.objects.filter(category__contains='10,').count()
    cards = Card.objects.filter(category__contains='10,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def octopus_card_aavs(request):
    number = Card.objects.filter(category__contains='11,').count()
    cards = Card.objects.filter(category__contains='11,')
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def citibank(request):
    number = Card.objects.filter(provider_id=8).count()
    cards = Card.objects.filter(provider_id=8)
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def standard_chartered(request):
    number = Card.objects.filter(provider_id=20).count()
    cards = Card.objects.filter(provider_id=20)
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def american_express(request):  # ===========================================
    number = Card.objects.filter(provider_id=3).count()
    cards = Card.objects.filter(provider_id=3)
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


def wewa_unionpay(request):  # ================================================
    number = Card.objects.filter(provider_id=8).count()
    cards = Card.objects.filter(provider_id=8)
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})


# ==========================================
def earnmore_unionpay_card(request):
    number = Card.objects.filter(provider_id=8).count()
    cards = Card.objects.filter(provider_id=8)
    providers = Provider.objects.all()
    return render(request, "cards.html", {"cards": cards, "providers": providers, "number": number})
