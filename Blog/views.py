from turtle import title
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


# Create your views here.
class BlogView(TemplateView):
    template_name = "./pages/blog.html"

    def get(self, request, blogTitle):
        _blogTitle = " ".join(blogTitle.split("-"))
        blog = get_object_or_404(Blog, title = _blogTitle)
        recentBlogs = Blog.objects.exclude(title = _blogTitle).order_by('releaseDate')
        return render(request, self.template_name, {
            'blog': blog,
            'recentBlogs': recentBlogs
        })

def ListBlog(request):
    template_name = './pages/listBlog.html'
    blogs = Blog.objects.all().order_by('releaseDate')

    paginator = Paginator(blogs, 6)
    if (request.GET.get('page')):
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1

    return render(request, template_name, {
        'blogs': paginator.page(page_number).object_list,
        'paginator': paginator,
        'currentPage': paginator.page(page_number)
    })