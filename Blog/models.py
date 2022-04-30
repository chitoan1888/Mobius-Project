from django.db import models
from django.contrib.postgres.fields import ArrayField
from tinymce import models as tinymce_models
import uuid, datetime

def create_phoneThumbnail_directory(instance, filename):
    dirname = instance.id
    return "blog/{}/thumb/{}".format(dirname, filename)

# Create your models here.
class Blog(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    shortDescription = models.CharField(max_length=500, default=None, null=True, blank=True)
    content = tinymce_models.HTMLField(max_length=None)
    releaseDate = models.DateField(default=datetime.date.today, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=create_phoneThumbnail_directory, default=None)
    likes = models.IntegerField(default=0)
    keywordsSearch = ArrayField(
        models.CharField(max_length=50),
    )
    def __str__(self):
        return self.title