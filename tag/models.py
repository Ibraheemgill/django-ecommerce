from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey 

# Create your models here.
class Tag(models.Model):
    labels=models.CharField(max_length=255)

class Tagged_items(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    # we have two ways here one is to import model from store.models and other is to use content type
    # using content types we can create generic relations between our apps/models

    content_type=models.ForeignKey(ContentType ,on_delete=models.CASCADE)

    object_id=models.PositiveIntegerField()
    content_object= GenericForeignKey()
