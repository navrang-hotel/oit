from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView 
from django.contrib.auth.decorators import login_required

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

#@login_required
# TODO: Need to add auth+permission required mixin
def projectDetail(request):
    """View function for project detail page."""

    template = 'ocprm/odashboard_detail.html'
    context = {}

    return render(request, template, context)

#@login_required
# TODO: Need to add auth+permission required mixin
class ProjectList(ListView):
    """View class for project list page."""

    model = Project
    template_name = 'ocprm/odashboard_list.html'

    def get_queryset(self):
        """Get the queryset for current user only."""
        
        user = self.request.user
        project_list = Project.objects.filter(actors=user)
        return project_list

def support(request):
    """View function for support page."""

    template = 'ocprm/odashboard_support.html'
    context = {}

    return render(request, template, context)

