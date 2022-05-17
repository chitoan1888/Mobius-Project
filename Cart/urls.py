from django.urls import path
from .views import getCart, postPhonetoCart, updatePhonetoCart

urlpatterns = [
    path('get/ajax/cart/', getCart, name="get_cart"),
    path('post/ajax/cart/', postPhonetoCart),
    path('update/ajax/cart/', updatePhonetoCart),
]