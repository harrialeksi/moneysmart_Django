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
            loan_usp = LoanUsp.objects.create(
                dd=usp['ratio'], dt=usp['text'], loan_id=row.id)
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

    if assoc != None:
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
                  {"Title": "Loans", "h3": "Get the Best HK Personal Installment Loans Rates and Offers Today",
                   "p": "Compare personal loans in Hong Kong. Pick the best APR and apply through Crediboo to get exclusive offers and cashback now!",
                   "cards": queryset, "providers": banks, "number": number, "provider_caption": "Banks", 'prov': bank, "filter_caption": "Loan Features", "filters": filters, "assoc": assoc})


def scbloans(request):
    loans = Loan.objects.prefetch_related(
        'loan_usp').filter(title__contains='standard')
    title = "Best Standard Chartered Personal Loans in Hong Kong 2022"
    desctiption = "International bank Standard Chartered offers several personal loans in Hong Kong, including a tax loan and a debt consolidation loan. Before you apply for any of them, read this guide to Standard Chartered loans to find out which is best for your needs."
    subtitle = ""
    sub_desc = ""
    categories = []
    broadcrump = "Standard Chartered Personal Loan Hong Kong 2022"
    return render(request, "pages/loans/best-standard-chartered-personal-loan-ms.html",
                  {"section": "Personal Loan", "url": "../personal-loan", "broadcrump": broadcrump, "title": title, "description": desctiption, "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "loans": loans, "title0": "Standard Chartered Personal Loan", "title1": "Standard Chartered Debt Consolidation Loan",
                   "snippet0": "Standard Chartered's personal loan is characterized by as low as 1.98% APR, high loan amount (up to HK$2,000,000/ 18x salary), 7-day cooling period and exclusive online offers of up to HK$2,000 cash coupons. Standard Chartered Bank also offers a designated calculator for applicants to quickly work out the repayment amount for better planning. Applicants can choose a repayment period between 12 months to 60 months. If the application is submitted before noon, it will be processed on the same day.",
                   "snippet1": "The Standard Chartered Debt Consolidation Program helps lender consolidates multiple bill payments into one simple repayment plan to reduce the overall interest. This plan features a monthly flat rate of as low as 0.0920% and an APR of as low as 2.15% with 0% handling fee. Lenders can borrow up to 18 times your monthly income or HK$2,000,000 (whichever is lower) and enjoy the option to repay over 6 years (72 months) to repay Standard Chartered. Standard Chartered will analyze lenders’ finances and tailor a repayment plan with a personalized interest rate. Standard Chartered will also follow up within the same business day as long as your application is submitted by noon."
                   })


def welendloans(request):
    loans = Loan.objects.prefetch_related('loan_usp').filter(id__in=[7, 31])
    title = "Best WeLend Personal Loans in Hong Kong 2022"
    desctiption = "WeLend is a licensed money lender in Hong Kong that launched in 2013. Unlike traditional banks and money lenders, WeLend is an online business that uses technology to make borrowing money faster and easier, with most of the personal loan process taking place online."
    subtitle = "Which WeLend Loan is Best for You?"
    sub_desc = "Click to jump to a specific section"
    categories = [{"link": "Best WeLend Personal Loan", "category": "Best welend personal loan",
                   "desc": "WeLend Personal Loan"},
                  {"link": "", "category": "Fast approval welend loan",
                   "desc": "WeLend No Document Loan"},
                  {"link": "WeLend Debt Consolidation Loan", "category": "welend debt consolidation loan",
                   "desc": "WeLend Card Debt Consolidation Loan"}]
    broadcrump = "Best WeLend Personal Loan Hong Kong 2022"
    return render(request, "pages/loans/best-welend-personal-loan-ms.html",
                  {"section": "Personal Loan", "url": "../personal-loan", "broadcrump": broadcrump, "title": title, "description": desctiption, "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "loans": loans, "title0": "Best WeLend Personal Loan", "title1": "WeLend Debt Consolidation Loan",
                   "snippet0": "WeLend Personal Loan is the most flexible loan option out of the three offerings. You can choose your desired repayment period from 14 days up to 60 months. Yes, you read right - 14 days! That's way shorter than a bank loan, where loan tenures are usually at least one year.<br><br>Your actual maximum loan amount is personalized based on your profile - WeLend assesses your credit score, monthly income, occupation, and financial situation. In theory, WeLend is able to lend any amount from HK$3,000 to HK$600,000.<br><br>Likewise, interest rates are customized for each applicant. You can get your personalized quote instantly by filling in an online application form. WeLend’s website also features a calculator tool so you can estimate repayment amounts for different loan tenures.<br><br>The eligibility criteria for WeLend personal loans is quite stringent. You need to be a Hong Kong resident, at least 18 years old, and be employed at your current job for at least two months, earning at least HK$8,000 a month.<br><br>*Calculation based on loan amount of HK$600,000 and repayment period of 12 months; the actual APR may vary for individual customers.",
                   "snippet1": "Like many banks and lending companies, one of WeLend's offerings is a Card Debt Consolidation Loan, a special type of personal loan where WeLend clears multiple credit card debts in one shot, freeing you up to repay WeLend according to your preferred schedule. Not only does this improve your cash flow, it also helps your credit score and saves on the high interest you would otherwise pay on your credit card bills.<br><br>When you submit your loan application online, WeLend uses what they call an A.I. Card Debt Master to assess your credit profile automatically and calculate three repayment plans tailored to your profile. Each of the three options is optimized to reduce the interest paid, reduce the monthly installment amounts, or reduce the time taken to repay the loan.<br><br>hose who meet WeLend's credit requirements may also opt for a 'phased' debt consolidation plan, which clears upcoming debts as well as current outstanding ones.<br><br>Eligibility requirements for this loan are the same: You must be a Hong Kong resident, at least 18 years old, employed at your current job for at least two months, and earning at least HK$8,000 a month.<br><br>Note: The final loan amount approved by WeLend and the loan tenure is evaluated on a case by case basis. Please submit your details to WeLend for your personalized quote.<br><br>*Calculation based on loan amount of HK$600,000 and repayment period of 12 months; the actual APR may vary for individual customers."
                   })


def citibank(request):
    loan = Loan.objects.prefetch_related('loan_usp').get(id=20)
    title = "Best Citibank Personal Loans in Hong Kong 2022"
    desctiption = "As a globally-recognised bank, Citibank is one of the go-to banks in Hong Kong for those looking to borrow money from a legitimate source. Citibank offers a range of personal loans to suit diverse needs, including a tax loan and a debt consolidation loan."
    subtitle = "Which Citibank Loan is Best for You?"
    sub_desc = "Click to jump to a specific section"
    categories = [{"link": "", "category": "citibank personal loan",
                   "desc": "Citi Tax Season Loan"},
                  {"link": "Citibank Debt Consolidation Loan", "category": "citibank debt consolidation loan",
                   "desc": "Citi Card Debt Consolidation Loans"}]
    broadcrump = "Best Citibank Personal Loan Hong Kong 2022"
    return render(request, "pages/loans/best-citibank-personal-loan-ms.html",
                  {"section": "Personal Loan", "url": "../personal-loan", "broadcrump": broadcrump, "title": title, "description": desctiption, "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "loan": loan, "title0": "Citibank Debt Consolidation Loan",
                   "snippet0": "If you're struggling with credit card debt that exceeds half of your total monthly earnings, it makes financial sense to get the Citibank Card Debt Consolidation Loans.<br><br>This is a special type of loan where the bank clears your high-interest credit card debts on your behalf, while you focus on repaying your Citibank loan with a repayment plan that suits you.<br><br>You can borrow up to 21 times your monthly salary (capped at HK$1,200,000) and can take up to to 60 months to pay it back.<br><br>Note: The final loan amount approved by Citibank and the loan tenure is evaluated on a case by case basis. Please contact Citibank for details.<br><br>*APR as low as 2.91% (calculation based on the monthly flat rate 0.13% with loan amount of HK$1,200,000 and repayment period of 12 months); the actual APR may vary for individual customers."
                   })


def dbs(request):
    loan = Loan.objects.prefetch_related('loan_usp').get(id=1)
    title = "Best DBS Personal Loans in Hong Kong 2022"
    desctiption = "Originally from Singapore, DBS Bank is now one of the top 10 largest banks in Hong Kong. DBS offers a range of personal loan options in Hong Kong, including a standard instalment loan and a debt consolidation loan. Find out which is best for you."
    subtitle = "Which DBS Loan is Best for You?"
    sub_desc = "Click to jump to a specific section"
    categories = [{"link": "", "category": "dbs personal loan",
                   "desc": "DBS Personal Instalment Loan"},
                  {"link": "", "category": "dbs debt consolidation loan",
                   "desc": "DBS Debt Consolidation Program"},
                  {"link": "DBS Revolving Loan", "category": "dbs revolving loan",
                   "desc": "DBS Cashline Revolving Loan"}]
    broadcrump = "Best DBS Personal Loan Hong Kong 2022"
    return render(request, "pages/loans/best-dbs-personal-loan-ms.html",
                  {"section": "Personal Loan", "url": "../personal-loan", "broadcrump": broadcrump, "title": title, "description": desctiption, "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "loan": loan, "title0": "DBS Revolving Loan",
                   "snippet0": "Unlike the DBS Personal Instalment Loan and Debt Consolidation Loan, the DBS Cashline Revolving Loan does not have a fixed repayment schedule.<br><br>Instead, DBS Cashline works more like a credit card. You will get a credit limit set by the bank - this can be up to 8 times your monthly salary or HK$800,000, whichever is lower.<br><br>You can choose to withdraw from that credit limit by either a Cashline card or cheque book (both provided). Only the amount that you withdraw will be subject to interest. But, as with a credit card, you need to repay it as soon as possible to avoid incurring high interest, which is charged daily. Once you repay the amount, the credit limit will be restored and you can redraw the amount at any time.<br><br>Given the distinct nature of the revolving loan, it only makes sense to go for this type of loan if you are very confident that you can repay the amount in a very short time. Otherwise, you may decide to convert your Cashline credit limit into a regular instalment loan (12 to 60 months) for a more manageable loan structure.<br><br>DBS Cashline Revolving Loan eligibility requirements are similar to that of the DBS Personal Instalment Loan. You must be a Hong Kong resident, at least 18 years old, and earning at least HK$80,000 a year."
                   })


def quickloan(request):
    loans = Loan.objects.prefetch_related(
        'loan_usp').filter(id__in=[6, 3, 7, 17, 12])
    title = "Best Quick Loans in Hong Kong 2022"
    desctiption = "Quick loan products are designed to provide immediate solutions for cash emergencies. Cash can usually be transferred without the hour. These products usually come with smaller loan amounts."
    subtitle = "Looking for the Best Quick Loan in Hong Kong?"
    sub_desc = "New to Quick Loan Application? Check out the best quick loan summary below:"
    categories = [{"link": "", "category": "comparison",
                   "desc": "Best Quick Loans"},
                  {"link": "howtoapply", "category": "application guide",
                   "desc": "How to Apply"},
                  {"link": "DBS Revolving Loan", "category": "got questions?",
                   "desc": "FAQ on quick loans"}]
    broadcrump = "Best Quick Cash Loans in Hong Kong:Get Cash Now"
    return render(request, "pages/loans/best-quick-loan-in-hong-kong-ms.html",
                  {"section": "Personal Loan", "url": "../personal-loan", "broadcrump": broadcrump, "title": title, "description": desctiption, "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "loans": loans, "title0": "Quick Cash Loans in HK",
                   })


def lowinterest(request):
    loans = Loan.objects.prefetch_related('loan_usp').filter(id__in=[3, 7, 10])
    title = "Low Interest Rate Loan in HK 2023"
    desctiption = "Looking for personal loans with low interest rate? Check out the best low interest rate loan below and FAQs before getting a loan."
    subtitle = "Best loan plans with low interest rate"
    sub_desc = ""
    categories = [{"link": "lowinterest", "category": "what you need to know before getting a loan:",
                   "desc": "Low interest rate loan?"},
                  {"link": "apr", "category": "what you need to know before getting a loan:",
                   "desc": "Annual Percentage Rates(APR)"},
                  {"link": "DBS Revolving Loan", "category": "got questions?",
                   "desc": "FAQ on low interest rate loans"}]
    broadcrump = "Low Interest Rate Loan 2022"
    return render(request, "pages/loans/low-interest-rate-loan-ms.html",
                  {"section": "Personal Loan", "url": "../personal-loan", "broadcrump": broadcrump, "title": title, "description": desctiption, "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "loans": loans, "title0": "Best Low Interest Rate Loans in HK",
                   "descriptions": ["DBS Personal Instalment Loan offers APR as low as 1.56%. If you are looking for bank loans with low interest rates, this is for sure your best choice!",
                                    "Looking for easy approval low interest rate loans? WeLend Personal Loan may be your best option! No income proof is required for loan amount less than HK$300,000!",
                                    "Looking for instantly approved loans with low interest rates? Try PrimeCredit Fixed Loan - their APR is at 2.38% and application can be approved immediately with loan sizes less than HK$50,000"]})


def online(request):
    loans = Loan.objects.prefetch_related(
        'loan_usp').filter(id__in=[3, 7, 12, 14])
    title = "Get Online Loans in HK: Instantly Approved Low Interest Loans"
    desctiption = "There are a wide range of personal loans available in the market. To make the entire loan application process easier, most banks and moneylenders have introduced online loans. Online loans are characterised by instant approval, lower interest rate, free from documents, etc. MoneySmart has put together a summary for you to have a better grasp of the different online loans available in the market."
    subtitle = "Online Loans - What Do You Need To Know?"
    sub_desc = "Don’t forget to read the sections below when comparing different online loans in the market."
    categories = [{"link": "pros", "category": "pros of online loans",
                   "desc": "What is the difference between online loans and general personal loans? Is the application open on weekends?"},
                  {"link": "compare", "category": "compare loans",
                   "desc": "Compare Online Loan Providers in HK"},
                  {"link": "", "category": "compare loans",
                   "desc": "Best Instant Approval Loans"},
                  {"link": "trust", "category": "must read before applying",
                   "desc": "Can you trust Money Lenders?"},
                  {"link": "", "category": "must read before applying",
                   "desc": "Online Loans FAQ"},
                  ]
    broadcrump = "Best Online Loans in HK: Instant Approval & Low-Interest"
    return render(request, "pages/loans/online-loans-ms.html",
                  {"section": "Personal Loan", "url": "../personal-loan", "broadcrump": broadcrump, "title": title, "description": desctiption, "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "loans": loans, "title0": "Online Loans offers",
                   "tds": [{"url": "./best-welend-personal-loan-ms", "bank": "Welend", "feature": "Infinite A.I. seamless, fully-online experience from quotation, approval and disbursement", "loan": "Column No income or address proof required for HK$300,000 or below3"},
                           {"url": "./?provider=26", "bank": "UA Finance", "feature": "Established in 1993 and a member of Sun Hung Kai Properties",
                               "loan": "No need to show up for loan application, no documents are required"},
                           {"url": "./?provider=23", "bank": "PrimeCredit", "feature": "Led by China Travel Financial Investment and formed by Pepper Group and York Capital Management Global Advisors",
                               "loan": "Online instant loan approval and 24x7 cash delivery"},
                           {"url": "./?provider=24", "bank": "Promise",
                               "feature": "Established in 1992 and a member of Sumitomo Mitsui Financial Group (SMFG) - one of the leading finance institutions in Japan.", "loan": "No supporting document is required, apply for a loan with HKID and mobile number only."},
                           {"url": "./best-dbs-personal-loan-ms", "bank": "DBS Bank", "feature": "Can apply online or via mobile apps",
                               "loan": "Interest rate as low as 1.56% and instant approval"},
                           {"url": "./?provider=8", "bank": "Citibank", "feature": "Can apply online or via telephone", "loan": "Interest rate as low as 1.78% and same day approval"}],
                   "td2s": [{"url": "#", "loan": "Promise Easy Loan", "APR": "As low as 4.49%", "contract": "Online"},
                           {"url": "#", "loan": "UA i-Money Express Online Personal Loan", "APR": "As low as 6.18%","contract": "Online"},
                           {"url": "#", "loan": "PrimeCredit Fixed Loan", "APR": "As low as 2.38%","contract": "online"},
                           {"url": "#", "loan": "DBS Personal Instalment Loan","APR": "As low as 1.56%", "contract": "Online"},
                           {"url": "#", "loan": "Citi Speedy Cash", "APR": "As low as 1.78%","contract": "Online"}]})


def apr(request):
    loans = Loan.objects.prefetch_related(
        'loan_usp').filter(id__in=[3, 7, 45])
    title = "All You Need to Know About Annual percentage rate (APR)"
    desctiption = "Top tips for borrowing money? Don’t only look at the interest rate! If you want to compare the true costs of borrowing, you should always refer to the Annual percentage rate (APR) instead of the interest rate. Not sure what APR is? Read on to find out more about APR."
    subtitle = ""
    sub_desc = ""
    categories = []
    broadcrump = "All You Need to Know About Annual percentage rate (APR)"
    return render(request, "pages/loans/what-is-apr-ms.html", {"section":"Personal Loan", "broadcrump": broadcrump, "title": title, "description": desctiption, "subtitle": subtitle, "sub_desc": sub_desc, "categories": categories, "loans":loans, "title0":"Low APR Loans in Hong Kong"})
