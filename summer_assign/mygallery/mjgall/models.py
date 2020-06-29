from django.db import models
from datetime import datetime

# Create your models here.

class photo(models.Model):
    objects = models.Manager()
    name = models.TextField(default = "PHOTO_NAME",blank=True)
    about = models.TextField(default = "ABOUT_PHOTO",blank=True)
    when = models.DateTimeField(default=datetime.now, blank=True)
    pic = models.ImageField(upload_to = "image", blank=True)

