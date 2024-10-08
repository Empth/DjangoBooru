from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone

class ImagePost(models.Model):

    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000, blank=True)
    created_date = models.DateTimeField("created date", default=timezone.now)
    modified_date = models.DateTimeField("modified date", default=timezone.now)
    tags = TaggableManager(blank=False)

    def __str__(self):
        if self.image:
            return self.image.url
        else:
            # can't reach but its fine, in case blank=True for image so
            # ImagePost doesn't break
            return 'None'
        
    def update_tags(self, new_tags):
        """
        Updates current set of tags with new tags from new_tags
        new_tags: array of strings representing tags
        """
        for tag in self.tags.all():
            if tag not in new_tags:
                self.tags.remove(tag)
        for tag in new_tags:
            self.tags.add(tag)
