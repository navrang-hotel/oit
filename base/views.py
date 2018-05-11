from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from django.views.generic.detail import DetailView 
from django.contrib.auth.decorators import login_required

from .models import Project

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

# *** No used now ***
def ologin(request):
    """View function for google verification."""

    template = 'base/login.html'
    context = {}

    return render(request, template, context)

@login_required
def dashboard(request):
    """View function for dashboard."""

    template = 'base/dashboard.html'
    context = {}

    return render(request, template, context)

@login_required
def uprofile(request):
    """View function for uprofile."""

    template = 'base/uprofile.html'

    # Get projects of this user
    user = request.user
    project_list = Project.objects.all().filter(
        user=user
    )

    context = {
        'project_list': project_list,
    }


    return render(request, template, context)

class ProjectDetailView(DetailView):
    """View class for project detail view."""

    model = Project
    template_name = 'base/uproject_detail.html'



