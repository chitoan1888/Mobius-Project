from .views import HomeView, search
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('search/', views.search, name='search_results'),
    path('', HomeView.as_view(), name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)