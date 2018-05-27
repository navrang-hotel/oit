from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ohotel-index'),
    path('staff/', views.staff_home, name='ohotel-staff-home'),
    path('staff/room/', views.staff_room, name='ohotel-staff-room'),
]

