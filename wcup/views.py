from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from .models import Player, Group
from .models import NepNews, Blog, BlogComment
from .forms import PlayerForm, BlogCommentForm

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    """View function for index page."""

    template = 'wcup/index.html'

    group_list = Group.objects.all()

    context = {
        'group_list': group_list,
    }

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

class NepNewsList(ListView):
    """View class for NepNewsList."""

    model = NepNews
    template_name = 'wcup/nepnews_list.html'

class BlogListView(ListView):
    """View class for blog list."""

    model = Blog
    template_name = 'wcup/blog_list.html'

class BlogDetailView(DetailView):
    """View class for blog detail."""

    model = Blog
    template_name = 'wcup/blog_detail.html'

def blog_comment_create(request, pk):
    """View function for creating a blog comment."""

    template = 'wcup/blog_comment_create.html'

    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data['comment_body']
            blog = Blog.objects.get(id=pk)
            bc = BlogComment(
                blog = blog,
                body = body,
            ) 
            bc.save()
            return HttpResponseRedirect(
                reverse('wcup-blog-detail', args=[pk])
            )
    else:
        form = BlogCommentForm()

    context = {
        'form': form,
    }
        
    return render(request, template, context)

