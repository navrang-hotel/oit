from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='realst-index'),
    path('homeloans/', views.home_loan, name='realst-homeloan'),
    path('aboutus/', views.about_us, name='realst-aboutus'),
    path('contactus/', views.contact_us, name='realst-contactus'),
    path('pricing/', views.pricing, name='realst-pricing'),
]

