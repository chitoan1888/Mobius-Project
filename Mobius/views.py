from re import search
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from Phone.models import Phone
from Blog.models import Blog
from Accessory.models import Accessory


class HomeView(TemplateView):
    template_name = "./pages/home.html"

    def get(self, request):
        phones = Phone.objects.order_by('dayOfManufacture')
        accessories = Accessory.objects.order_by('dayOfManufacture')
        blogs = Blog.objects.order_by('releaseDate')
        return render(request, self.template_name, {
            'phones': phones,
            'accessories': accessories,
            'blogs': blogs,
        })

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(price__icontains=query) | Q(brand__icontains=query) | Q(description__icontains=query) | Q(keywordsSearch__icontains=query)
            results= Phone.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'components/search_results.html', context)
        else:
            return render(request, 'components/search_results.html')
    else:
        return render(request, 'components/search_results.html')







