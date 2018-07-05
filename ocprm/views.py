from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project, StartProjectRequestD, GetSupportTicket
from .models import ProjectComment

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


@login_required
def support(request):
    """View function for support page."""

    template = 'ocprm/odashboard_support.html'
    context = {}

    return render(request, template, context)

def pdf_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

class GetSupportTicketCreate(CreateView):
    """View class for get support ticket create page."""

    template_name = 'ocprm/odashboard_support.html'

    model = GetSupportTicket
    #fields = '__all__'
    fields = [
        'title',
        'description',
    ]

    def get_success_url(self):
        #return reverse('ocprm-gsr-success', args=[self.kwargs['pk']])
        return reverse('ocprm-gsr-success', args=[self.object.id])

    def form_valid(self, form):
        """
        Add user and associated project to form data before setting it as valid.
        """
        #Add logged-in user as raiser
        form.instance.user = self.request.user
        form.instance.status = 'N'
        #Associate comment with project based on passed id
        form.instance.project = get_object_or_404(Project, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(GetSupportTicketCreate, self).form_valid(form)

def support_request_success(request, pk):
    """View function for support request success message."""

    template = 'ocprm/gsrsuccess.html'
    context = {
        'pk': pk,
    }

    return render(request, template, context)
   
class StartProjectRequestCreate(CreateView):
    """View class for creating start project request."""

    model = StartProjectRequestD
    template_name = 'ocprm/start_project.html'
    fields = [
        'status',
        'project_type',
        'description',
    ]

    def get_success_url(self):
        #return reverse('ocprm-spr-success')
        return reverse('ocprm-spr-success', args=[self.object.id])

    def form_valid(self, form):
        """
        Add user and associated project to form data before setting it as valid.
        """
        form.instance.user = self.request.user
        #form.instance.status = 'N'
        return super(StartProjectRequestCreate, self).form_valid(form)

def start_project_success(request, pk):
    """View function for start project success message."""

    template = 'ocprm/sprsuccess.html'
    context = {
        'pk': pk,
    }

    return render(request, template, context)

class ProjectCommentCreate(CreateView):
    """View class for project comment create page."""

    template_name = 'ocprm/project_comment_create.html'

    model = ProjectComment
    fields = [
        'body',
    ]

    def get_success_url(self):
        return reverse('ocprm-project-detail', args=[self.kwargs['pk']])

    def form_valid(self, form):
        """
        Add user and other info to form data before setting it as valid.
        """
        form.instance.commentor = self.request.user
        form.instance.project = get_object_or_404(Project, pk = self.kwargs['pk'])
        return super(ProjectCommentCreate, self).form_valid(form)

