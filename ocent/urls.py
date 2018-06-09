from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ocent-index'),
    #path('userprofile/', views.userProfile, name='base-userprofile'),
]

