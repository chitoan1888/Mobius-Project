from django.urls import path
from .views import checkout

urlpatterns = [
    path('order/checkout/', checkout, name="checkout"),
]