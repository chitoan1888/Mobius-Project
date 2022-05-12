from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Phone, PhoneImage
from django.shortcuts import get_object_or_404

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