##
 # base/urls.py:
 #
 # St: 2018-04-27 Fri 04:36 PM
 # Up: 2018-04-27 Fri 04:36 PM
 #
 # Author: SPS
 ##

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='base-index'),
    path('services/', views.services, name='base-services'),
    path('about/', views.about, name='base-about'),
    path('careers/', views.careers, name='base-careers'),
    path('contact/', views.contact, name='base-contact'),
    path('google756697d741e49fcc.html', views.googleVerify, name='base-google-verify'),
    path('sitemap.txt', views.googleSitemap, name='base-google-sitemap'),
    path('ologin/', views.ologin, name='base-ologin'),
    path('dashboard/', views.dashboard, name='base-dashboard'),
    path('dashboard/uprofile', views.uprofile, name='base-dashboard-uprofile'),
]

