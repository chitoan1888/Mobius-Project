from django.urls import path
from .views import ProductView, getAccessoryDetail, ListAccessory

urlpatterns = [
    path('phu-kien/', ListAccessory.as_view(), name="listAccessory"),
    path('phu-kien/<str:accessoryName>/', ProductView.as_view(), name="accessoryView"),
    path('get/ajax/accessory/<str:accessoryId>/', getAccessoryDetail, name="get_accessory")
]