from .views import HomePageView, search
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]