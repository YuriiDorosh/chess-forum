import uuid

from django.db import models



class BaseModel(models.Model):
    """Basic Model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True
        ordering = ('-date_added',)