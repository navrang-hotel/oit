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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ContactMessage, JobVacancy
from .models import IndexPageHeader, IndexPageHeroPara, IndexPageMain, IndexPagePartner
from .models import IndexPageServices
from .models import OITAddress, ContactPageExistingCustomer, ContactPageFollowUs
from .models import ContactPageWriteMessage, ContactPageHeader
from .models import CareersPageHero, CareersPageReasons

from ocprm.models import StartProjectRequest
from .forms import ContactMessageForm, UserRegistrationForm
from ocprm.forms import StartProjectRequestForm

def index(request):
    """View function for index page."""

    template = 'base/index.html'

    iph = IndexPageHeader.objects.get(id=1)
    iphp = IndexPageHeroPara.objects.get(id=1)
    ipm = IndexPageMain.objects.get(id=1)
    ipp = IndexPagePartner.objects.get(id=1)
    ips = IndexPageServices.objects.get(id=1)

    context = {
        'iph': iph,
        'iphp': iphp,
        'ipm': ipm,
        'ipp': ipp,
        'ips': ips,
    }

    return render(request, template, context)

def services(request):
    """View function for services page."""

    template = 'base/services.html'
    context = {}

    return render(request, template, context)

def careers(request):
    """View function for careers page."""

    template = 'base/careers.html'

    crph = CareersPageHero.objects.get(id=1)
    crpr = CareersPageReasons.objects.get(id=1)

    context = {
        'crph': crph,
        'crpr': crpr,
    }

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

def open_source_projects(request):
    """View function for open source projects page."""

    template = 'base/open_source_projects.html'
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
    form_class = ContactMessageForm

    def get_success_url(self):
        """Override success url."""

        return reverse('base-contact-success')

    def get_context_data(self, **kwargs):
        """Override success url."""

        oit_address = OITAddress.objects.get(id=1)
        cph = ContactPageHeader.objects.get(id=1)
        cpwm = ContactPageWriteMessage.objects.get(id=1)
        cpec = ContactPageExistingCustomer.objects.get(id=1)
        cpfu = ContactPageFollowUs.objects.get(id=1)
        context = super(ContactMessageCreate, self).get_context_data(**kwargs)
        context['cph'] = cph
        context['oit_address'] = oit_address
        context['cpwm'] = cpwm
        context['cpec'] = cpec
        context['cpfu'] = cpfu
        return context

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

def faq(request):
    """View function for faq page."""

    template = 'base/faq.html'
    context = {}

    return render(request, template, context)

def support(request):
    """View function for support page."""

    template = 'base/support.html'
    context = {}

    return render(request, template, context)

class UserRegister(CreateView):
    """View class for user registration page."""

    template_name = 'register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        """Override success url."""

        return reverse('base-index')

def user_register(request):
    """View function for user registration page."""

    template = 'register.html'

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            # check if user already exists
            user_exists = check_user_exists(email)
            if user_exists == True: 
                email_exist_err = 'Email already exists.'
                context = {
                    'form': form,
                    'email_exist_err': email_exist_err,
                }
                return render(request, template, context)
            else:
                u = User.objects.create_user(
                    username,
                    email,
                    password1
                ) 
                u.save()
                return HttpResponseRedirect(reverse('base-user-register-success'))
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, template, context)

def userRegistrationSuccess(request):
    """View function for user registration success."""

    template = 'base/user_register_success.html'
    context = {}

    return render(request, template, context)

def terms(request):
    """View function for terms page."""

    template = 'base/terms.html'
    context = {}

    return render(request, template, context)

@login_required
def userProfile(request):
    """View function for user profile page."""

    template = 'base/user_profile.html'


    context = {}

    return render(request, template, context)
    


