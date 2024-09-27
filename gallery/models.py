from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone

class ImagePost(models.Model):

    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000, blank=True)
    created_date = models.DateTimeField("created date", default=timezone.now)
    modified_date = models.DateTimeField("modified date", default=timezone.now)
    tags = TaggableManager(blank=True)

    def __str__(self):
        if self.image:
            return self.image.url
        else:
            return 'None'
