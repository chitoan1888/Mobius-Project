from django.urls import path
from .views import ProductView, getPhoneDetail

urlpatterns = [
    path('dien-thoai/<str:phoneName>/', ProductView.as_view(), name="phoneView"),
    path('get/ajax/phone/<str:phoneId>/', getPhoneDetail, name="get_phone")
]