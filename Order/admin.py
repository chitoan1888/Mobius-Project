from django.contrib import admin
from .models import Order, OrderItem

class CartItemAdmin(admin.StackedInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'get_totlalItem', 'created_at', 'totalPrice', 'isPaid', 'paidTime')
    inlines = [CartItemAdmin]

    class Meta:
       model = Order

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'  #Renames column head

    def get_totlalItem(self, obj):
        return self.inlines.__len__;
    get_totlalItem.short_description = 'Total products'  #Renames column head

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass