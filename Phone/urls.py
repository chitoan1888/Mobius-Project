from django.urls import path
from .views import ProductView

urlpatterns = [
    path('dien-thoai/<str:phoneName>/', ProductView.as_view())
]