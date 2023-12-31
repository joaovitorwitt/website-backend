from django.db import models

# Create your models here.

class Articles(models.Model):
    class Meta:
        db_table = "Articles"

    
    # description
    # timestamp
    # content
    # thumbnail
    # content
    # images inside the content


    def __str__(self):
        return self.title
