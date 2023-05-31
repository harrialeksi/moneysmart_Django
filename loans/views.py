from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Prefetch, Case, When, Value, BooleanField, Count, Q
from utils.scrape.scrape import get_cards
from .models import Loan, LoanUsp, Feature, Bank

def get_loans(category, bank):
    if category == None:
        if bank == "0" or bank == None:
            number = Loan.objects.count()
            queryset = Loan.objects.prefetch_related('loan_usp').all()[:20]
        else:
            number = Loan.objects.filter(bank_id=bank).count()
            queryset = Loan.objects.prefetch_related(
                'loan_usp').filter(bank_id=bank)[:20]
    else:
        if category == 11:
            query = str(category)
        else:
            query = str(category) + ','
        if bank == "0" or bank == None:
            number = Bank.objects.filter(category__contains=query).count()
            queryset = Bank.objects.filter(
                category__contains=query).prefetch_related('loan_usp').all()[:20]
        else:
            number = Loan.objects.filter(category__contains=query).filter(
                bank_id=bank).count()
            queryset = Loan.objects.filter(category__contains=query).prefetch_related(
                'loan_usp').filter(bank_id=bank)[:20]
    return number, queryset


def loans(request, category=None):
    url = 'https://www.moneysmart.hk/en/personal-loan'
    bank = request.GET.get('provider')
    # loans = get_cards(url)

    # # Delete all rows in CardDetail, CardUsp table
    # LoanUsp.objects.all().delete()

    # for loan in loans:
    #     row = Loan.objects.get(title=loan['title'])
    #     row.image = loan['img_src']
    #     row.disclosure = loan['disclosure']
    #     row.execlusive = loan['badge_execlusive']
    #     row.badge_label = loan['badge_label']
    #     row.badge_primary = loan['badge_primary']
    #     row.snippet = loan['snippet']
    #     row.snippet_img = loan['snippet_img']
    #     row.promotion = loan['promotion']
    #     row.keyfeatures = loan['keyFeatures']
    #     row.repayment = loan['repayment']
    #     row.save()

    #     for usp in loan['usp']:
    #         loan_usp = LoanUsp.objects.create(dd=usp['ratio'], dt=usp['text'], loan_id=row.id)
    #         loan_usp.save()

    # Retrieve all cards joined with their related card details
   
    banks = Bank.objects.all()
    number, queryset = get_loans(category, bank)
    filters = Feature.objects.all()

    return render(request, "pages/loans/loans.html", {"cards": queryset, "number": number, "provider_caption":"Banks", "providers": banks, 'prov': bank, "filter_caption":"Loan Features", "filters":filters})


def airport_lounge_access(request):
    title = "Best Credit Cards for Airport Lounges in Hong Kong"
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

    return render(request, "pages/popular-guides_credit-cards-for-airport-lounge-access.html", {"broadcrump": broadcrump, "title": title, "description": desctiption,
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

    return render(request, "pages/hotel_reward_booking.html", {"broadcrump": broadcrump, "title": title, "description": desctiption,
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