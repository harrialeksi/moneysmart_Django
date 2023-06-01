from django.shortcuts import render

# Create your views here.
def dining(request, category=None):
    # Retrieve all cards joined with their related card details
    # number, queryset = get_accounts(category)

    return render(request, "pages/blogs/blog-dining.html")
