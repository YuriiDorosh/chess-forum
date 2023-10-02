import uuid

from django.db import models

from versatileimagefield.fields import VersatileImageField


class BaseModel(models.Model):
    """Basic Model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True
        ordering = ('-date_added',)
        
class BaseImage(models.Model):
    """Basic model for images"""

    title = models.CharField(max_length=200, null=True, blank=True)
    alt = models.CharField(max_length=200, null=True, blank=True)
    image = VersatileImageField(null=True, blank=True, upload_to="images")

    class Meta:
        abstract = True
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        res = ""
        if self.title:
            res = self.title
        else:
            res = self.image.url
        return res