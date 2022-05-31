from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid

from Phone.models import Phone
from Accessory.models import Accessory


class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isPaid = models.BooleanField(default=False)
    totalPrice = models.IntegerField(default=0)
    paidTime = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

class OrderItem(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True, blank=True)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
