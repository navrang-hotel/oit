from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='milano-index'),
    path('products/', views.products, name='milano-products'),
    path('dealers/', views.dealers, name='milano-dealers'),
    path('about/', views.about, name='milano-about'),
    path('contact/', views.contact, name='milano-contact'),
    path('mycart/', views.mycart, name='milano-mycart'),
]

