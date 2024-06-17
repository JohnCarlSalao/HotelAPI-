import uuid
from django.db import models

class Hotel(models.Model):
    uid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    hotel_name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    hotel_image = models.ImageField(null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Hotels'
        
    def __str__(self):
        return self.hotel_name