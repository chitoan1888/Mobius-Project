from django.http import HttpResponse, JsonResponse
from .models import Cart, CartItem
from Phone.models import Phone
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.db.models import Q


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def getCart(request):
    if is_ajax(request=request) and request.method == "GET" and request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        cartItems = CartItem.objects.filter(cart=cart)
        data = {
            'cartItems': serializers.serialize('json', cartItems)
        }
        return JsonResponse(data, status = 200)

    return JsonResponse({}, status = 400)

def postPhonetoCart(request):
    if is_ajax(request=request) and request.method == "POST" and request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        phone = get_object_or_404(Phone, id=request.POST.get('phoneId'))
        CartItem.objects.create(
            phone = phone,
            quantity = request.POST.get('quantity'),
            cart = cart,
        )
        return JsonResponse({"result": "success"}, status=200)
    return JsonResponse({"result": "failed"}, status=400)

def updatePhonetoCart(request):
    if is_ajax(request=request) and request.method == "POST" and request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        phone = get_object_or_404(Phone, id=request.POST.get('phoneId'))
        cartItem = CartItem.objects.filter(Q(cart=cart) & Q(phone=phone))

        cartItem.update(
            quantity = cartItem.first().quantity + 1,
        )
        return JsonResponse({"result": "success"}, status=400)
    return JsonResponse({"result": "failed"}, status=400)