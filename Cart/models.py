from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from Phone.models import Phone
from Accessory.models import Accessory


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class CartItem(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True, blank=True)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)