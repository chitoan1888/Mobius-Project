from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Phone, PhoneImage
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
import json
from django.core.paginator import Paginator

# template render
class ProductView(TemplateView):
    template_name = "./pages/product.html"

    def get(self, request, phoneName):
        _phoneName = " ".join(phoneName.split("-"))
        phone = get_object_or_404(Phone, name= _phoneName)
        phoneImages = PhoneImage.objects.filter(phone=phone)
        return render(request, self.template_name, {
            'product': phone,
            'productImages': phoneImages,
            'productType': 1
        })

def ListPhone(request):
    template_name = "./pages/listProduct.html"

    phone = Phone.objects.all()
    brand = request.GET.get('brand')
    price = None


    if (request.GET.get('price')):
        price = json.loads(request.GET.get('price'))
        minPrice = int(price['minPrice'])
        maxPrice = int(price['maxPrice'])


    if (brand != None):
        phone = phone.filter(brand=brand).order_by("dayOfManufacture")


    if (price != None):
        phone = phone.filter(price__gte=minPrice, price__lte=maxPrice).order_by("price")

    # order
    if (request.GET.get('order')):
        order = int(request.GET.get('order'))
        match order:
            case 1:
                phone = phone.order_by("price")
            case 2:
                phone = phone.order_by("-price")
            case 3:
                phone = phone.order_by("-dayOfManufacture")
            case 4:
                phone = phone.order_by("-sold")

    paginator = Paginator(phone, 12)
    if (request.GET.get('page')):
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    return render(request, template_name, {
        'title': 'Điện thoại',
        'products': paginator.page(page_number).object_list,
        'productType': 'phone',
        'paginator': paginator,
        'currentPage': paginator.page(page_number)
    })

# ajax request
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