from django.contrib import admin
from .models import Cart, CartItem

class CartItemAdmin(admin.StackedInline):
    model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_totlalItem')
    inlines = [CartItemAdmin]

    class Meta:
       model = Cart

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'  #Renames column head

    def get_totlalItem(self, obj):
        return self.inlines.__len__;
    get_totlalItem.short_description = 'Total products'  #Renames column head

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass