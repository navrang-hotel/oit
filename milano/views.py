from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

def index(request):
    """View function for index page."""

    template = 'milano/index.html'
    context = {}

    return render(request, template, context)

def products(request):
    """View function for products page."""

    template = 'milano/products.html'
    context = {}

    return render(request, template, context)

def dealers(request):
    """View function for dealers page."""

    template = 'milano/dealers.html'
    context = {}

    return render(request, template, context)

def about(request):
    """View function for about page."""

    template = 'milano/about.html'
    context = {}

    return render(request, template, context)

def contact(request):
    """View function for contact page."""

    template = 'milano/contact.html'
    context = {}

    return render(request, template, context)

