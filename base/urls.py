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
    #path('contact/', views.contact, name='base-contact'),
    path('contact/', views.ContactMessageCreate.as_view(), name='base-contact'),
    path('contact/success', views.contactMessageSuccess, name='base-contact-success'),
    path('google756697d741e49fcc.html', views.googleVerify, name='base-google-verify'),
    path('sitemap.txt', views.googleSitemap, name='base-google-sitemap'),
    path('ologin/', views.ologin, name='base-ologin'),
    #path('dashboard/', views.dashboard, name='base-dashboard'),
    #path('dashboard/uprofile/', views.uprofile, name='base-dashboard-uprofile'),
    #path('dashboard/uproject/<int:pk>/', views.ProjectDetailView.as_view(), name='base-dashboard-uproject'),
    path('documentation/', views.documentation, name='base-documentation'),
    path('opensource/', views.open_source_projects, name='base-opensource'),
    path('feedback/', views.feedback, name='base-feedback'),
    path('start/', views.ostart, name='base-start'),
    #path('project/', views.oproject, name='base-dashboard-project'),
    path('startproject/', views.start_project_request, name='base-start-project'),
    path('startproject/success', views.start_project_request_success, name='base-start-project-request-success'),
    path('careers/vacancy', views.JobVacancyList.as_view(), name='base-careers-vacancy-list'),
    path('careers/vacancy/<int:pk>', views.JobVacancyDetail.as_view(), name='base-careers-vacancy-detail'),
    path('faq/', views.faq, name='base-faq'),
    path('support/', views.support, name='base-support'),
    path('register/', views.user_register, name='base-user-register'),
    path('register/success', views.userRegistrationSuccess, name='base-user-register-success'),
    path('terms/', views.terms, name='base-terms'),
    path('userprofile/', views.userProfile, name='base-userprofile'),
    path('whatyouget/', views.what_you_get, name='base-whatyouget'),
    path('foodo/', views.foo_foo, name='base-foo'),
    path('foodo/success', views.foo_success, name='base-foo-success'),
    path('subscriber/add/', views.add_subscriber, name='base-subscriber-add'),
    path('subscriber/success/', views.subscribe_success, name='base-subscribe-success'),
    path('ajax/validate_username/', views.validate_username, name='base-validate-username'),
    path('ajax/subscriber_add/', views.subscriber_add_ajax, name='base-subscriber-add-ajax'),
]

