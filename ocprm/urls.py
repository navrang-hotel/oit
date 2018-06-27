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
    path('support/', views.support, name='ocprm-support'),
    path('pdftest/', views.pdf_view, name='ocprm-pdftest'),
]

