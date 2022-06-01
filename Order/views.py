from django.shortcuts import render
from Cart.models import Cart, CartItem

# Create your views here.
def checkout(request):
    template_name = './pages/order.html'

    if request.method == 'POST':
        if request.user.is_authenticated():
            print(request.POST.get('address'))

    return render(request, template_name)

