from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid, datetime

from django.forms import DateField

def create_phoneImage_directory(instance, filename):
    dirname = instance.phone.name
    return "phones/{}/images/{}".format(dirname, filename)

def create_phoneThumbnail_directory(instance, filename):
    dirname = instance.name
    return "phones/{}/thumb/{}".format(dirname, filename)

class Phone(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, default='')
    dayOfManufacture = models.DateField(default=datetime.date.today, blank=True, null=True)
    insurance = models.DateField(default=datetime.date.today, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=create_phoneThumbnail_directory, default=None)
    description = models.TextField(max_length=None)
    price = models.IntegerField(default=0)
    saleOff = models.FloatField(default=0)
    likes = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    keywordsSearch = ArrayField(
        models.CharField(max_length=50),
    )
    def __str__(self):
        return self.name

class PhoneImage(models.Model):
    phone = models.ForeignKey(Phone, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=create_phoneImage_directory)

    def __str__(self):
        return self.phone.name