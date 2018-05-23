from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from .models import Player 
from django.http import HttpResponseRedirect

from .forms import PlayerForm

def index(request):
    """View function for index page."""

    template = 'wcup/index.html'
    context = {}

    return render(request, template, context)

def player_create(request):
    """View function for creating a player."""

    template = 'wcup/player_create.html'

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['player_first_name']
            last_name = form.cleaned_data['player_last_name']
            p = Player(
                first_name = first_name,
                last_name = last_name
            ) 
            p.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = PlayerForm()

    context = {
        'form': form,
    }
        
    return render(request, template, context)

