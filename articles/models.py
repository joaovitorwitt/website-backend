from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

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
    


# class ContentImagesInsideArticles(models.Model):
#     class Meta:
#         db_table = "Article Images"


#     article = models.ForeignKey(Articles, on_delete=models.CASCADE)
#     images = models.CharField(max_length=255)
#     short_description = models.CharField(max_length=255)

#     def __str__(self):
#         return f"Image for {self.title}"
