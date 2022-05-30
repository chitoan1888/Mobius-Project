from turtle import title
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404


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