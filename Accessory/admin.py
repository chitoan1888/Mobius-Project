from django.contrib import admin
from .models import Accessory, AccessoryImage


class AccessoryImageAdmin(admin.StackedInline):
    model = AccessoryImage

@admin.register(Accessory)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'description', 'dayOfManufacture', 'insurance', 'price', 'likes', 'sold', 'keywordsSearch')
    inlines = [AccessoryImageAdmin]
    class Meta:
       model = Accessory

    class Media:
        js = ['/js/tiny_mce.js']


@admin.register(AccessoryImage)
class AccessoryImageAdmin(admin.ModelAdmin):
    pass
