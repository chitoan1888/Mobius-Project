from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Accessory, AccessoryImage
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
import json
from django.core.paginator import Paginator


# template render
class ProductView(TemplateView):
    template_name = "./pages/product.html"

    def get(self, request, accessoryName):
        _accessoryName = " ".join(accessoryName.split("-"))
        accessory = get_object_or_404(Accessory, name= _accessoryName)
        accessoryImages = AccessoryImage.objects.filter(accessory=accessory)
        return render(request, self.template_name, {
            'product': accessory,
            'productImages': accessoryImages,
            'productType': 2
        })

def ListAccessory(request):
    template_name = "./pages/listProduct.html"

    accessory = Accessory.objects.all()
    brand = request.GET.get('brand')
    price = None
    accessoryCategory = request.GET.get('accessoryCategory')


    if (request.GET.get('price')):
        price = json.loads(request.GET.get('price'))
        minPrice = int(price['minPrice'])
        maxPrice = int(price['maxPrice'])


    if (brand != None):
        accessory = accessory.filter(brand=brand).order_by("dayOfManufacture")


    if (price != None):
        accessory = accessory.filter(price__gte=minPrice, price__lte=maxPrice).order_by("price")

    if (accessoryCategory != None):
            accessory = accessory.filter(category=accessoryCategory).order_by("dayOfManufacture")


    # order
    if (request.GET.get('order')):
        order = int(request.GET.get('order'))
        match order:
            case 1:
                accessory = accessory.order_by("price")
            case 2:
                accessory = accessory.order_by("-price")
            case 3:
                accessory = accessory.order_by("-dayOfManufacture")
            case 4:
                accessory = accessory.order_by("-sold")

    paginator = Paginator(accessory, 12)
    if (request.GET.get('page')):
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    return render(request, template_name, {
        'title': 'Ph??? ki???n',
        'products': paginator.page(page_number).object_list,
        'productType': 'accessory',
        'paginator': paginator,
        'currentPage': paginator.page(page_number)
    })

# ajax request
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def getAccessoryDetail(request, accessoryId):
    if is_ajax(request=request) and request.method == "GET":
        accessory = Accessory.objects.filter(id=accessoryId)
        data = {
            'accessory': serializers.serialize('json', accessory, fields=('name', 'thumbnail', 'price',  'saleOff'))
        }
        return JsonResponse(data, status = 200)

    return JsonResponse({}, status = 400)