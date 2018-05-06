from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

def index(request):
    """View function for index page."""

    template = 'base/index.html'
    context = {}

    return render(request, template, context)

def services(request):
    """View function for services page."""

    template = 'base/services.html'
    context = {}

    return render(request, template, context)

def careers(request):
    """View function for careers page."""

    template = 'base/careers.html'
    context = {}

    return render(request, template, context)

def contact(request):
    """View function for contact page."""

    template = 'base/contact.html'
    context = {}

    return render(request, template, context)

def about(request):
    """View function for about page."""

    template = 'base/about.html'
    context = {}

    return render(request, template, context)

def googleVerify(request):
    """View function for google verification."""

    template = 'base/google756697d741e49fcc.html'
    context = {}

    return render(request, template, context)

def googleSitemap(request):
    """View function for google verification."""

    template = 'base/sitemap.txt'
    context = {}

    return render(request, template, context)

