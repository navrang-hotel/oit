from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .models import ContactMessage, JobVacancy
from ocprm.models import StartProjectRequest
from .forms import ContactMessageForm
from ocprm.forms import StartProjectRequestForm

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

#@login_required
#def dashboard(request):
#    """View function for dashboard."""
#
#    template = 'base/odashboard.html'
#    context = {}
#
#    return render(request, template, context)

#@login_required
#def uprofile(request):
#    """View function for uprofile."""
#
#    template = 'base/uprofile.html'
#
#    # Get projects of this user
#    user = request.user
#    project_list = Project.objects.all().filter(
#        user=user
#    )
#
#    context = {
#        'project_list': project_list,
#    }
#
#
#    return render(request, template, context)

#class ProjectDetailView(DetailView):
#    """View class for project detail view."""
#
#    model = Project
#    template_name = 'base/oproject_detail.html'

def documentation(request):
    """View function for documentation page."""

    template = 'base/documentation.html'
    context = {}

    return render(request, template, context)

def feedback(request):
    """View function for feedback page."""

    template = 'base/feedback.html'
    context = {}

    return render(request, template, context)

def ostart(request):
    """View function for ostart page."""

    template = 'base/ostart.html'
    context = {}

    return render(request, template, context)

class ContactMessageCreate(CreateView):
    """View class for creating contact message."""

    template_name = 'base/contact.html'
    model = ContactMessage
    # fields = [
    #     'sender_name',
    #     'sender_email',
    #     'message',
    # ]
    form_class = ContactMessageForm

    def get_success_url(self):
        """Override success url."""

        return reverse('base-contact-success')

def contactMessageSuccess(request):
    """View function for contact message success."""

    template = 'base/contact_success.html'
    context = {}

    return render(request, template, context)

class StartProject(CreateView):
    """View class for start project page."""

    template_name = 'base/start_project.html'

    model = StartProjectRequest
    form_class = StartProjectRequestForm

    def get_success_url(self):
        """Override success url."""

        return reverse('base-contact-success')

def check_user_exists(email):
    """Non view helper function to check if user exists."""

    if User.objects.filter(email=email).exists():
        return True
    
    return False

def start_project_request(request):
    """View function for start project page."""

    template = 'base/start_project.html'

    if request.method == 'POST':
        form = StartProjectRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            project_type = form.cleaned_data['project_type']
            description = form.cleaned_data['description']
            # check if user already exists
            user_exists = check_user_exists(email)
            if user_exists == True: 
                return HttpResponseRedirect(reverse('login'))
            spr = StartProjectRequest(
                email = email,
                project_type = project_type,
                status = 'P',
                description = description,
            ) 
            spr.save()
            return HttpResponseRedirect(reverse('base-start-project-request-success'))
    else:
        form = StartProjectRequestForm()

    context = {
        'form': form,
    }

    return render(request, template, context)

def start_project_request_success(request):
    """View function for start project request success."""

    template = 'base/start_project_request_success.html'
    context = {}

    return render(request, template, context)

def job_vacancy(request):
    """View function for job vacancy."""

    template = 'base/job_vacancy.html'
    context = {}

    return render(request, template, context)

class JobVacancyList(ListView):
    """View class for job vacancy."""

    template_name = 'base/job_vacancy.html'
    model = JobVacancy

class JobVacancyDetail(DetailView):
    """View class for job vacancy detail."""

    template_name = 'base/job_vacancy_detail.html'
    model = JobVacancy

