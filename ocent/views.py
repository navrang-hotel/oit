from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """View function for index page."""

    template = 'ocent/index.html'

    context = {}

    return render(request, template, context)

