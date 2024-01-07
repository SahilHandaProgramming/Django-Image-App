from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Image(models.Model):
    imageName=models.CharField(max_length=50)
    mainImage = models.FileField(upload_to="imagesFolder/")
    category=models.CharField(max_length=50)
    imageSlug = AutoSlugField(populate_from="imageName",unique=True)