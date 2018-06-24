from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from reportlab.pdfgen import canvas

from .models import Project

@login_required
def index(request):
    """View function for index page."""

    template = 'ocprm/odashboard_home.html'

    # Get projects of this user
    user = request.user
    project_list = Project.objects.all().filter(
        projectusercontext__user=user
    )
    
    context = {
        'project_list': project_list,
    }

    return render(request, template, context)

class ProjectList(LoginRequiredMixin, ListView):
    """View class for project list page."""

    model = Project
    template_name = 'ocprm/odashboard_list.html'

    def get_queryset(self):
        """Get the queryset for current user only."""
        
        user = self.request.user
        project_list = Project.objects.filter(actors=user)
        return project_list

# TODO: Need to add auth+permission required mixin
@login_required
def projectDetail(request):
    """View function for project detail page."""

    template = 'ocprm/odashboard_detail.html'
    context = {}

    return render(request, template, context)

class ProjectDetail(LoginRequiredMixin, DetailView):
    """View class for project detail page."""

    model = Project
    template_name = 'ocprm/odashboard_detail.html'


def support(request):
    """View function for support page."""

    template = 'ocprm/odashboard_support.html'
    context = {}

    return render(request, template, context)

