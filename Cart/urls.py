from django.urls import path
from .views import getCart, postProductToCart, updateProductToCart, removeProductFromCart, OrderView

urlpatterns = [
    path('get/ajax/cart/', getCart, name="get_cart"),
    path('post/ajax/cart/<int:product_type>', postProductToCart),
    path('remove/ajax/cart/<int:product_type>', removeProductFromCart),
    path('update/ajax/cart/<int:product_type>', updateProductToCart),
    path('order', OrderView.as_view(), name="order")
]