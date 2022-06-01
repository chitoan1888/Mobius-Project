from django.http import JsonResponse
from .models import Cart, CartItem
from Phone.models import Phone
from Accessory.models import Accessory
from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.db.models import Q
from django.views.generic import TemplateView


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def getCart(request):
    if is_ajax(request=request) and request.method == "GET" and request.user.is_authenticated:
        print(request.GET)
        cart = get_object_or_404(Cart, user=request.user)
        cartItems = CartItem.objects.filter(cart=cart)
        totalPrice = 0

        for cartItem in cartItems:
            if (cartItem.phone != None):
                totalPrice += (cartItem.phone.price - cartItem.phone.price * cartItem.phone.saleOff) * cartItem.quantity
            else:
                totalPrice += (cartItem.accessory.price - cartItem.accessory.price * cartItem.accessory.saleOff) * cartItem.quantity

        data = {
            'cartItems': serializers.serialize('json', cartItems),
            'totalPrice': totalPrice
        }
        return JsonResponse(data, status = 200)

    return JsonResponse({}, status = 400)

def postProductToCart(request, product_type):
    if is_ajax(request=request) and request.method == "POST" and request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        if (int(product_type) == 1):
            phone = get_object_or_404(Phone, id=request.POST.get('productId'))
            CartItem.objects.create(
                phone = phone,
                quantity = request.POST.get('quantity'),
                cart = cart,
            )
        else:
            accessory = get_object_or_404(Accessory, id=request.POST.get('productId'))
            CartItem.objects.create(
                accessory = accessory,
                quantity = request.POST.get('quantity'),
                cart = cart,
            )
        return JsonResponse({"result": "success"}, status=200)
    return JsonResponse({"result": "failed"}, status=400)

def updateProductToCart(request, product_type):
    if is_ajax(request=request) and request.method == "POST" and request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        if (int(product_type) == 1):
            phone = get_object_or_404(Phone, id=request.POST.get('productId'))
            cartItem = CartItem.objects.filter(Q(cart=cart) & Q(phone=phone))
        else:
            accessory = get_object_or_404(Accessory, id=request.POST.get('productId'))
            cartItem = CartItem.objects.filter(Q(cart=cart) & Q(accessory=accessory))

        cartItem.update(
            quantity = cartItem.first().quantity + 1,
        )
        return JsonResponse({"result": "success"}, status=200)
    return JsonResponse({"result": "failed"}, status=400)

def removeProductFromCart(request, product_type):
    if is_ajax(request=request) and request.method == "POST" and request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)

        if (int(product_type) == 1):
            phone = get_object_or_404(Phone, id=request.POST.get('productId'))
            CartItem.objects.filter(Q(cart=cart) & Q(phone=phone)).delete()
        else:
            accessory = get_object_or_404(Accessory, id=request.POST.get('productId'))
            CartItem.objects.filter(Q(cart=cart) & Q(accessory=accessory)).delete()

        return JsonResponse({"result": "success"}, status=200)
    return JsonResponse({"result": "failed"}, status=400)

class OrderView(TemplateView):
    template_name = './pages/order.html'