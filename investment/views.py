from django.shortcuts import render
from django.db.models import Q
from utils.scrape.scrape import get_data
from .models import Investment, InvestmentUsp, Category, Provider, Promotion, HeroSection

def scrape_investment(url):
    cards = get_data(url)

    # Delete all rows in CardDetail, CardUsp table
    InvestmentUsp.objects.all().delete()

    for card in cards:
        row = Investment.objects.get(title=card['title'])
        row.image = card['img_src']
        row.disclosure = card['disclosure']
        row.execlusive = card['badge_execlusive']
        row.badge_label = card['badge_label']
        row.badge_primary = card['badge_primary']
        row.snippet = card['snippet']
        row.snippet_img = card['snippet_img']
        row.promotion = card['promotion']
        row.keyfeatures = card['keyFeatures']
        row.accountopening = card['accountopening']
        row.commissionfees = card['commissionfees']
        row.save()

        for usp in card['usp']:
            car_usp = InvestmentUsp.objects.create(dd=usp['ratio'], dt=usp['text'], card_id=row.id)
            car_usp.save()

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
    provider = request.GET.get('provider')
    providers = Provider.objects.all()

    # Retrieve all cards joined with their related card details
    number, queryset = get_investments(category, provider)
    filters = Promotion.objects.all()
    heros = HeroSection.objects.all()

    return render(request, "pages/investments/investments.html", 
                  {"Title":"Investment", "Heros":heros, "MoreIndex":8, "h3":"Best Online Brokerages in Hong Kong 2023", "p":"Choose from MoneySmart's curated list of best brokerage accounts in Hong Kong! <br> Getting started to invest and need a stock trading account? Compare and find the best online investment brokerage stock account in Hong Kong in terms of fees and commission, platform capabilities and product portfolios. Learn how to open an investment brokerage account and start investing today!",
                    "cards": queryset, "number": number, "provider_caption":"Providers", "providers": providers, "prov": provider, "feature_caption":"Online Brokerage Features", "filter_caption":"Promotions", "filters":filters})
