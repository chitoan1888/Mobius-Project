from re import search
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Phone
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = './pages/home.html'

# def search(request):
#     searched = request.POST.get('searched')
#     name = Phone.objects.filter(Q(name__icontains=searched))
#     price = Phone.objects.filter(Q(price__icontains=searched))


#     context = {
#         'name': name,
#         'price': price,
#         'searched': searched,
#     }

#     return render(request, 'search_results.html', context)

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(price__icontains=query) | Q(brand__icontains=query) | Q(description__icontains=query) | Q(keywordsSearch__icontains=query)
            results= Phone.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'search_results.html', context)
        else:
            return render(request, 'search_results.html')
    else:
        return render(request, 'search_results.html')







