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

def time_deposit_ms(request):
    accounts = Account.objects.prefetch_related('account_usp').filter(id__in=[1,3,4,6])
    return render(request, "pages/accounts/time-deposit-ms.html",
                  {"accounts":accounts,"tds1": [{"bank":"Citiplus", "annual":"5.4%", "term":"1 month", "mindeposit":"HK$50,000", "mininterest":"HK$219"},
                            {"bank":"HSBC", "annual":"3.4%", "term":"12 months", "mindeposit":"HK$10,000", "mininterest":"HK$340"},
                            {"bank":"Bank of China", "annual":"7%", "term":"7 days", "mindeposit":"HK$50,000", "mininterest":"HK$67.12"},
                            {"bank":"DBS", "annual":"3.0%", "term":"12 months", "mindeposit":"HK$50,000", "mininterest":"HK$1500"},
                            {"bank":"CMB Wing Lung", "annual":"3.85%", "term":"6 months", "mindeposit":"HK$100,000", "mininterest":"HK$1925"},
                            {"bank":"Bank of Communications", "annual":"3.5%", "term":"6 months", "mindeposit":"HK$20,000", "mininterest":"HK$350"},
                            {"bank":"China CITIC Bank (International)", "annual":"3.6%", "term":"3 months", "mindeposit":"HK$10,000", "mininterest":"HK$90"},
                            {"bank":"Standard Chartered Bank", "annual":"3.6%", "term":"12 months", "mindeposit":"HK$10,000", "mininterest":"HK$360"},
                            {"bank":"", "annual":"As of 3rd Apr 2023", "term":"", "mindeposit":"", "mininterest":""},
                            ],
                    "tds2": [{"bank":"FusionBank", "annual":"3.4%", "term":"6 months", "mindeposit":"HK$1", "mininterest":"HK$168.58"},
                            {"bank":"WeLab Bank", "annual":"3.8%", "term":"12 months", "mindeposit":"HK$10", "mininterest":"HK$380"},
                            {"bank":"airstar", "annual":"3.1%", "term":"6 months", "mindeposit":"HK$1,000", "mininterest":"HK$153.82"},
                            {"bank":"ZA Bank", "annual":"3.31%", "term":"12 months", "mindeposit":"HK$1", "mininterest":"HK$331"},
                            {"bank":"", "annual":"As of 3rd Apr 2023", "term":"", "mindeposit":"", "mininterest":""},
                            ],
                    "tds3": [{"bank":"Citibank(Citigold)", "6mon":"2.87%", "6interest":"HK$14,350", "12mon":"N/A", "12interest":"N/A", "additional":""},
                            {"bank":"Hang Seng Bank", "6mon":"4.68%", "6interest":"HK$23,400", "12mon":"N/A", "12interest":"N/A", "additional":"N/A"},
                            {"bank":"ICBC (Asia)", "6mon":"4.6%", "6interest":"HK$23,000", "12mon":"4.6%", "12interest":"HK$46,000", "additional":"N/A"},
                            ],
                            })

