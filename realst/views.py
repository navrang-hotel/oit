from django.shortcuts import render

# Create your views here.

# ============
# Added by dev
# ============

def index(request):
    """View function for index page."""

    template = 'realst/index.html'
    context = {}

    return render(request, template, context)

def home_loan(request):
    """View function for home loan page."""

    template = 'realst/home_loans.html'
    context = {}

    return render(request, template, context)

def about_us(request):
    """View function for about us page."""

    template = 'realst/about_us.html'
    context = {}

    return render(request, template, context)

def contact_us(request):
    """View function for contact us page."""

    template = 'realst/contact_us.html'
    context = {}

    return render(request, template, context)

def pricing(request):
    """View function for pricing page."""

    template = 'realst/pricing.html'
    context = {}

    return render(request, template, context)

