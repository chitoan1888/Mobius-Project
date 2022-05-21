from .views import register_request, login_request, logout_request
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("dang-nhap", views.login_request, name="dang-nhap"),
    path("dang-ki", views.register_request, name="dang-ki"),
    path("dang-xuat", views.logout_request, name= "dang-xuat")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)