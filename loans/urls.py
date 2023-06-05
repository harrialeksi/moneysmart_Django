from django.urls import path

from . import views

app_name = "loans"
urlpatterns = [
    path("", views.loans, name="loans"),
    path("<int:category>", views.loans, name="category"),
    path("best-standard-chartered-personal-loan-ms", views.scbloans, name="best_scb_personal_loans"),
    path("best-welend-personal-loan-ms", views.welendloans, name="best_welend_personal_loans"),
    path("best-citibank-personal-loan-ms", views.citibank, name="best_citibank_personal_loans"),
    path("best-dbs-personal-loan-ms", views.dbs, name="best_dbs_personal_loan_ms"),
    path("best-quick-loan-in-hong-kong-ms", views.quickloan, name="best_quick_loan_ms"),
    path("low-interest-rate-loan-ms", views.lowinterest, name="low_interest_rate_loan_ms"),
    path("online-loans-ms", views.online, name="online_loans_ms"),
    path("what-is-apr-ms", views.apr, name="apr_ms"),
]