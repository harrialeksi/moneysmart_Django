from django.shortcuts import render
from django.db.models import Q
from utils.scrape.scrape import get_data
from .models import Account, AccountUsp, Provider, HeroSection

def scrape_account(url):
    accounts = get_data(url)
    # Delete all rows in CardDetail, CardUsp table
    AccountUsp.objects.all().delete()

    for card in accounts:
        row = Account.objects.get(title=card['title'])
        row.image = card['img_src']
        row.disclosure = card['disclosure']
        row.execlusive = card['badge_execlusive']
        row.badge_label = card['badge_label']
        row.badge_primary = card['badge_primary']
        row.snippet = card['snippet']
        row.snippet_img = card['snippet_img']
        row.promotion = card['promotion']
        row.keyfeatures = card['keyFeatures']
        row.interestrate = card['interestRate']
        row.bonusinterestrate = card['bonusInterestRate']
        row.save()

        for usp in card['usp']:
            car_usp = AccountUsp.objects.create(dd=usp['ratio'], dt=usp['text'], card_id=row.id)
            car_usp.save()

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
    provider = request.GET.get('provider')
    providers = Provider.objects.all()

    # Retrieve all cards joined with their related card details
    number, queryset = get_accounts(category, provider)
    heros = HeroSection.objects.all()

    return render(request, "pages/accounts/accounts.html", 
                  {"Title":"Accounts", "Heros":heros, "MoreIndex":3, "h3":"Compare Best Savings Accounts in Hong Kong", "p":"Search for the best saving accounts to align with your personal saving goals and earn interest on your balance. <br> Start earning extra cash rebate with high deposit interest rate upon opening a savings account. Compare the minimum account balance and savings interest rate to find the one that suits your needs.",
                   "cards": queryset, "number": number, "provider_caption":"Providers", "providers": providers, "prov": provider})
