from django.db import models
from django.contrib.postgres.fields import ArrayField
from tinymce import models as tinymce_models
import uuid, datetime

def create_phoneImage_directory(instance, filename):
    dirname = instance.accessory.name
    return "accessory/{}/images/{}".format(dirname, filename)

def create_phoneThumbnail_directory(instance, filename):
    dirname = instance.name
    return "accessory/{}/thumb/{}".format(dirname, filename)

AccessoryCategory = (
    (1, "Tai nghe"),
    (2, "Loa"),
    (3, "Dây sạc"),
    (4, "Smartwatch")
)

Brands = (
    ("apple", "Apple"),
    ("asus", "Asus"),
    ("samsung", "Samsung"),
    ("huawei", "Huawei"),
    ("lg", "LG"),
    ("vivo", "Vivo"),
    ("xiaomi", "Xiaomi"),
    ("sony", "Sony"),
    ("jbl", "JBL")
)

class Accessory(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    brand = models.CharField(max_length=100, default='apple', choices=Brands)
    category = models.IntegerField(default=1, choices=AccessoryCategory)
    dayOfManufacture = models.DateField(default=datetime.date.today, blank=True, null=True)
    insurance = models.DateField(default=datetime.date.today, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=create_phoneThumbnail_directory, default=None)
    description = tinymce_models.HTMLField(max_length=None)
    price = models.IntegerField(default=0)
    saleOff = models.FloatField(default=0)
    likes = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    keywordsSearch = ArrayField(
        models.CharField(max_length=50),
    )
    def __str__(self):
        return self.name

class AccessoryImage(models.Model):
    accessory = models.ForeignKey(Accessory, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=create_phoneImage_directory)

    def __str__(self):
        return self.accessory.name