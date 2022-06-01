
from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site
from .views import HomeView, search
from django.views.defaults import page_not_found
import django

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),
    path("404/", custom_page_not_found),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home_view'),
    path('tim-kiem/', search, name='search_results'),
    path('', include('Phone.urls')),
    path('', include('Accessory.urls')),
    path('', include('User.urls')),
    path('', include('Cart.urls')),
    path('', include('Blog.urls')),
    path('', include('Order.urls')),
]
