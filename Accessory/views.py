from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import Accessory


class HomeView(TemplateView):
    template_name = "./pages/home.html"

    def get(self, request):
        accessories = Accessory.objects.all()
        return render(request, self.template_name, {'accessories': accessories})