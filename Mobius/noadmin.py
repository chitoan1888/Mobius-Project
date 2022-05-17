from django.urls import reverse
from django.http import HttpResponse, Http404
from django.utils.deprecation import MiddlewareMixin

class NoAdmin(MiddlewareMixin):

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def process_request(self, request):
        if request.path.startswith(reverse('admin:login')):
            if NoAdmin.get_client_ip(request) != "127.0.0.1":
                raise Http404