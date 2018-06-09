from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from django.views.generic.detail import DetailView 
from django.contrib.auth.decorators import login_required

from .models import Project

@login_required
def index(request):
    """View function for index page."""

    template = 'ocprm/odashboard_home.html'

    # Get projects of this user
    user = request.user
    project_list = Project.objects.all().filter(
        user=user
    )
    
    context = {
        'project_list': project_list,
    }

    return render(request, template, context)

#@login_required
# TODO: Need to add permission required mixin
class ProjectDetail(DetailView):
    """View class for project detail page."""

    model = Project
    template_name = 'ocprm/project_detail.html'

