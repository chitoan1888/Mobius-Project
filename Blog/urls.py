from django.urls import path
from .views import BlogView

urlpatterns = [
    path('tin-tuc/<str:blogTitle>/', BlogView.as_view(), name="blog_detail"),
]