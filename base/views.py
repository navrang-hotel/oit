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

