from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Phone, PhoneImage
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers


class ProductView(TemplateView):
    template_name = "./pages/product.html"

    def get(self, request, phoneName):
        _phoneName = " ".join(phoneName.split("-"))
        phone = get_object_or_404(Phone, name= _phoneName)
        phoneImages = PhoneImage.objects.filter(phone=phone)
        print(phoneImages)
        return render(request, self.template_name, {
            'product': phone,
            'productImages': phoneImages
        })

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def getPhoneDetail(request, phoneId):
    if is_ajax(request=request) and request.method == "GET":
        phone = Phone.objects.filter(id=phoneId)
        data = {
            'phone': serializers.serialize('json', phone, fields=('name', 'thumbnail', 'price'))
        }
        return JsonResponse(data, status = 200)

    return JsonResponse({}, status = 400)