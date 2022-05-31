from django.urls import path
from .views import BlogView, ListBlog

urlpatterns = [
    path('tin-tuc/', ListBlog, name='blog'),
    path('tin-tuc/<str:blogTitle>/', BlogView.as_view(), name="blog_detail"),
]