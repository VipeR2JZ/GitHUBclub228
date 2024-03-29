from django.urls import path

from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
    edit_profile,
    profile,
    HomePageView,
    SearchResultsView,
)

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('post/<int:pk>/delete/',
         BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/',
         BlogUpdateView.as_view(), name='post_edit'),
    path('', BlogListView.as_view(), name='home'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
]