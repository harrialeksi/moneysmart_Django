from django.shortcuts import render

# Create your views here.
def faq(request):

    return render(request, "pages/faqs/faqs.html")
