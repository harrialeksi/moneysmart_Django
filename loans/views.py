from django.shortcuts import render
from django.db.models import Q
from utils.scrape.scrape import get_data
from .models import Loan, LoanUsp, Bank

def scrape_loan(url):
    loans = get_data(url)

    # Delete all rows in CardDetail, CardUsp table
    LoanUsp.objects.all().delete()

    for loan in loans:
        row = Loan.objects.get(title=loan['title'])
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
    bank = request.GET.get('provider')
    banks = Bank.objects.all()
    
    # Retrieve all loans joined with their related card details
    number, queryset = get_loans(category, bank)

    return render(request, "pages/loans/loans.html", {"Title":"Loans", "cards": queryset, "providers": banks, "number": number, "provider_caption":"Banks", 'prov': bank})
