from .views import register_request, login_request, logout_request
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)