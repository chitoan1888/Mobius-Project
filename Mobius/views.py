from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.db.models import Q
from Phone.models import Phone
from Blog.models import Blog
from Accessory.models import Accessory
from Cart.models import Cart, CartItem



class HomeView(TemplateView):
    template_name = "./pages/home.html"

    def get(self, request):
        phones = Phone.objects.order_by('dayOfManufacture')
        accessories = Accessory.objects.order_by('dayOfManufacture')
        blogs = Blog.objects.order_by('releaseDate')
        cart = None
        cartItems = None
        if (request.user.is_authenticated):
            cart = get_object_or_404(Cart, user=request.user)
            cartItems = CartItem.objects.filter(cart=cart)

        return render(request, self.template_name, {
            'phones': phones,
            'accessories': accessories,
            'blogs': blogs,
            'cartItems': cartItems,
        })

def search(request):
    template_name = './pages/listProduct.html'

    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(price__icontains=query) | Q(brand__icontains=query) | Q(description__icontains=query) | Q(keywordsSearch__icontains=query)
            results= Phone.objects.filter(lookups).distinct()
            context={'products': results,
                     'submitbutton': submitbutton}
            return render(request, template_name, context)
        else:
            return render(request, template_name)
    else:
        return render(request, template_name)







