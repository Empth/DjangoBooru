from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone

class ImagePost(models.Model):

    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000, blank=True)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    tags = TaggableManager(blank=True)

    def __str__(self):
        if self.image:
            return self.image.url
        else:
            return 'None'
