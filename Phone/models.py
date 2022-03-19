from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

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
    description = models.TextField(max_length=None)
    likes = models.IntegerField(default=0);
    sold = models.IntegerField(default=0);
    price = models.IntegerField(default=0)
    keywordsSearch = ArrayField(
        models.CharField(max_length=50),
    )


# class Bills(models.Model):
#     id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4, editable=False)
#     itemList = models.ManyToManyField(Phone, related_name='itemList', blank=True)
#     def get_name_items(self):
#         return "\n".join([p.name for p in self.itemList.all()])