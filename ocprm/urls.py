##
 # ocprm/urls.py:
 #
 # St: 2018-04-27 Fri 04:36 PM *
 # Up: 2018-04-27 Fri 04:36 PM
 #
 # Author: SPS
 ##

from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProjectList.as_view(), name='ocprm-dashboard'),
    path('project/list/', views.ProjectList.as_view(), name='ocprm-project-list'),
    #path('projectdetail/', views.projectDetail, name='ocprm-project-detail'),
    path('projectdetail/<int:pk>/', views.ProjectDetail.as_view(), name='ocprm-project-detail'),
    path('project/<int:pk>/support', views.GetSupportTicketCreate.as_view(), name='ocprm-support'),
    path('pdftest/', views.pdf_view, name='ocprm-pdftest'),
    path('project/support/<int:pk>/success', views.support_request_success, name='ocprm-gsr-success'),
    path('project/start', views.StartProjectRequestCreate.as_view(), name='ocprm-project-start'),
    path('project/start/<int:pk>/success', views.start_project_success, name='ocprm-spr-success'),
    path('project/<int:pk>/comment', views.ProjectCommentCreate.as_view(), name='ocprm-project-comment'),
]

