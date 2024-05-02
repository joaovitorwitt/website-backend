###############################################################################
# Imports
###############################################################################
from django.db import models
from django.contrib.postgres.fields import ArrayField

###############################################################################
# Article Model Implementation
###############################################################################
class Articles(models.Model):
    class Meta:
        db_table = "Articles"

    thumbnail = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='')
    content_images = ArrayField(models.CharField(), blank=True, null=True)
    
    def __str__(self):
        return self.title

