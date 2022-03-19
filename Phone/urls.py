from .views import HomePageView, SearchResultsView
from django.urls import path

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]