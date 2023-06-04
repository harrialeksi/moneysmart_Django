from django.shortcuts import render
from django.db.models import Q
from utils.scrape.scrape import get_data
from .models import Account, AccountUsp, Provider, HeroSection

def scrape_account(url):
    accounts = get_data(url)
    # Delete all rows in CardDetail, CardUsp table
    AccountUsp.objects.all().delete()

    for account in accounts:
        row = Account.objects.get(title=account['title'])
        row.image = account['img_src']
        row.disclosure = account['disclosure']
        row.execlusive = account['badge_execlusive']
        row.badge_label = account['badge_label']
        row.badge_primary = account['badge_primary']
        row.snippet = account['snippet']
        row.snippet_img = account['snippet_img']
        row.promotion = account['promotion']
        row.keyfeatures = account['keyFeatures']
        row.interestrate = account['interestRate']
        row.bonusinterestrate = account['bonusInterestRate']
        row.bonuscashrebate = account['bonusCashRebate']
        row.save()

        for usp in account['usp']:
            account_usp = AccountUsp.objects.create(dd=usp['ratio'], dt=usp['text'], account_id=row.id)
            account_usp.save()

# Create your views here.
def get_accounts(category, provider):
    number = Account.objects
    queryset = Account.objects.prefetch_related('account_usp')

    if provider != "0" and provider != None:
        number = number.filter(provider_id=provider)
        queryset = queryset.filter(provider_id=provider)

    if category != None:
        query = str(category) + ','
        number = number.filter(category__contains=query)
        queryset = queryset.filter(category__contains=query)
        
    return number.count(), queryset.all()

def accounts(request, category=None):
    provider = request.GET.get('provider')
    providers = Provider.objects.all()

    # Retrieve all cards joined with their related card details
    number, queryset = get_accounts(category, provider)
    heros = HeroSection.objects.all()

    return render(request, "pages/accounts/accounts.html", 
                  {"Title":"Accounts", "Heros":heros, "MoreIndex":3, "h3":"Compare Best Savings Accounts in Hong Kong", "p":"Search for the best saving accounts to align with your personal saving goals and earn interest on your balance. <br> Start earning extra cash rebate with high deposit interest rate upon opening a savings account. Compare the minimum account balance and savings interest rate to find the one that suits your needs.",
                   "cards": queryset, "number": number, "provider_caption":"Providers", "providers": providers, "prov": provider})
