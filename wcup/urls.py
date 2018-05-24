from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='wcup-index'),
    path('player_create/', views.player_create, name='wcup-player-create'),
    path('nepnews_list/', views.NepNewsList.as_view(), name='wcup-nepnews-list'),
    path('blog/', views.BlogListView.as_view(), name='wcup-blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='wcup-blog-detail'),
]

