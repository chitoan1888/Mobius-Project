from django.contrib import admin
from .models import Phone
# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'likes', 'keywordsSearch') 


# @admin.register(Bills)
# class BillsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'get_name_items') 


