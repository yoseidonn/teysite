from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["title", "description", "date"]