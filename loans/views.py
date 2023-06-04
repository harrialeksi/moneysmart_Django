from django.shortcuts import render
from django.db.models import Q
from utils.scrape.scrape import get_data
from .models import Loan, LoanUsp, Bank, Feature


def scrape_loan(url):
    loans = get_data(url)

    # Delete all rows in CardDetail, CardUsp table
    LoanUsp.objects.all().delete()

    for loan in loans:
        row = Loan.objects.get(title=loan['title'], url=loan['url'])
        row.image = loan['img_src']
        row.disclosure = loan['disclosure']
        row.execlusive = loan['badge_execlusive']
        row.badge_label = loan['badge_label']
        row.badge_primary = loan['badge_primary']
        row.snippet = loan['snippet']
        row.snippet_img = loan['snippet_img']
        row.promotion = loan['promotion']
        row.keyfeatures = loan['keyFeatures']
        row.repayment = loan['repayment']
        row.save()

        for usp in loan['usp']:
            loan_usp = LoanUsp.objects.create(dd=usp['ratio'], dt=usp['text'], loan_id=row.id)
            loan_usp.save()

def get_loans(category, provider, assoc):
    number = Loan.objects
    queryset = Loan.objects.prefetch_related('loan_usp')

    if provider != "0" and provider != None:
        number = number.filter(bank_id=provider)
        queryset = queryset.filter(bank_id=provider)

    if category != None:
        query = str(category) + ','
        number = number.filter(category__contains=query)
        queryset = queryset.filter(category__contains=query)

    if assoc !=None:
        number = number.filter(feature__contains=assoc)
        queryset = queryset.filter(feature__contains=assoc)
        
    return number.count(), queryset.all()


def loans(request, category=None):
    bank = request.GET.get('provider')
    assoc = request.GET.get('assoc')
    banks = Bank.objects.all()
    filters = Feature.objects.all()
    # Retrieve all loans joined with their related card details
    number, queryset = get_loans(category, bank, assoc)

    return render(request, "pages/loans/loans.html", 
                  {"Title":"Loans", "h3":"Get the Best HK Personal Installment Loans Rates and Offers Today", 
                   "p":"Compare personal loans in Hong Kong. Pick the best APR and apply through Crediboo to get exclusive offers and cashback now!",
                   "cards": queryset, "providers": banks, "number": number, "provider_caption":"Banks", 'prov': bank, "filter_caption":"Loan Features", "filters":filters, "assoc": assoc})
