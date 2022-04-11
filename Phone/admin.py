from django.contrib import admin
from .models import Phone, PhoneImage


class PhoneImageAdmin(admin.StackedInline):
    model = PhoneImage

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'description', 'dayOfManufacture', 'insurance', 'price', 'likes', 'sold', 'keywordsSearch')
    inlines = [PhoneImageAdmin]
    class Meta:
       model = Phone

    class Media:
        js = ['/js/tiny_mce.js']

@admin.register(PhoneImage)
class PhoneImageAdmin(admin.ModelAdmin):
    pass

# @admin.register(Bills)
# class BillsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'get_name_items')


