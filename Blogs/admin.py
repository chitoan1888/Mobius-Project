from django.contrib import admin
from .models import Blogs
@admin.register(Blogs)
class Blogs(admin.ModelAdmin):
    list_display = ('title', 'releaseDate', 'likes', 'keywordsSearch')
    class Meta:
       model = Blogs
    class Media:
        js = ['/js/tiny_mce.js']

