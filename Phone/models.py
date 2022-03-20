from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid, datetime

from django.forms import DateField

# Create your models here.
# def create_directory(instance, filename):
#     dirname = instance.id
#     return "templates/{}/{}".format(dirname, filename)

# def create_imgs_directory(instance, filename):
#     dirname = instance.template.id
#     return "templates/{}/imgs/{}".format(dirname, filename)
    
class Phone(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, default='')
    dayOfManufacture = models.DateField(default=datetime.date.today, blank=True, null=True)
    insurance = models.DateField(default=datetime.date.today, blank=True, null=True)
    description = models.TextField(max_length=None)
    likes = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    keywordsSearch = ArrayField(
        models.CharField(max_length=50),
    )
    def __str__(self):
        return self.name
