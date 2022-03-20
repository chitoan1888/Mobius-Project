from django.db import models
from django.contrib.postgres.fields import ArrayField
from numpy import true_divide
from Phone.models import Phone
import datetime, uuid

# Create your models here.

# def create_imgs_directory(self, filename):
#         dirname = self.uid
#         return "userProfilePics/{}/{}".format(dirname, filename)

class UserInfo(models.Model):
    uid = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4, editable=False)
    displayName = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=50, unique=True, default='')
    password = models.CharField(max_length=20, default='')
    email = models.EmailField()
    # profilePic = models.ImageField(upload_to=create_imgs_directory, null=True)
    # defaultGooglePhotoUrl = models.CharField(max_length=200, default='', blank=True, null=True)
    phone = models.CharField(max_length=11, default='', null=True)
    GENDER_CHOICES = (
        ('M', 'Nam'),
        ('F', 'Nữ')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)
    dateOfBirth = models.DateField(default=datetime.date.today, blank=True, null=True)
    # comments = models.CharField(max_length=300, default='')

    shoppingCart = models.ManyToManyField(Phone, related_name='itemList', blank=True)
    # Display shoppingCart on admin page
    def items_in_shoppingCart(self):
        return "\n".join([p.name for p in self.shoppingCart.all()])

    wishList = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list
    )
    purchasedList = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list
    )
    def __str__(self):
        return self.displayName



