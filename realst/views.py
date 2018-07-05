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


