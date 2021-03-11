from django.db import models
from martor.models import MartorField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    thumbnail = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    title = models.CharField(max_length=255)
    body = MartorField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    
    def __str__(self):
        return f"{self.last_modified} - {self.title}"

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    