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
    path('', views.index, name='ocprm-dashboard'),
]

