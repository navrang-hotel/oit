from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='wcup-index'),
    path('player_create/', views.player_create, name='wcup-player-create'),
]

