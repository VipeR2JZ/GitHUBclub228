from django.urls import path
from .views import PostApiView,test_view

urlpatterns = [
    path('api/posts/', PostApiView.as_view(), name='post_api'),
    path('test/ ', test_view, name='test_view'),

    ]