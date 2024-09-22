from django.db import models
from taggit.managers import TaggableManager

class ImagePost(models.Model):

    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published")
    tags = TaggableManager()

    def __str__(self):
        return self.image.url
