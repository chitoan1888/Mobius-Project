
from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site
from .views import HomeView, search
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),

    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home_view'),
    path('search/', search, name='search_results'),
    # path('', include('Phone.urls')),
    path('', include('User.urls')),
    # path('', include('Blogs.urls')),
]
