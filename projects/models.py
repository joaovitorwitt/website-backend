###############################################################################
# Imports
###############################################################################
from django.db import models

###############################################################################
# Project Model Implementation
###############################################################################
class Projects(models.Model):
    class Meta:
        db_table = "Projects"

    project_id = models.AutoField(primary_key=True)
    # project_image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    project_image_url = models.CharField(max_length=255)
    project_title = models.CharField(max_length=255)
    project_description = models.TextField()
    
    def __str__(self):
        return self.title