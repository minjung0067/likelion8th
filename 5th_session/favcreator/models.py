from django.db import models

class Youtuber(models.Model):
    channel_name = models.CharField(max_length=30)
    creator_name = models.CharField(max_length=30)
    likes = models.IntegerField()
    onair = models.BooleanField()
    subscriber = models.IntegerField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()


