from django.contrib import admin
from .models import Blog
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('title', 'releaseDate', 'likes', 'keywordsSearch')
    class Meta:
       model = Blog
    class Media:
        js = ['/js/tiny_mce.js']

