from django.db import models
from django.utils import timezone

# Create your models here.

class Articles(models.Model):
    class Meta:
        db_table = "Articles"

    thumbnail = models.ImageField(upload_to='article_thumbnails/', null=True, blank=True)
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='')
    
    def __str__(self):
        return self.title
    


class ContentImagesInsideArticles(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article_content_images/')
    short_description = models.CharField(max_length=255)

    def __str__(self):
        return f"Image for {self.title}"
