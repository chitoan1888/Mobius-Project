from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Phone
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Phone
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Phone.objects.filter(
            Q(name__icontains=query) | Q(price__icontains=query)
        )
        return object_list
        