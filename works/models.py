from django.db import models
from martor.models import MartorField
import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='uploads/')
    category = models.CharField(max_length=4, choices=[('PRT','Portofolio'), ("IDE",'Idea')])
    created_at = models.DateField(default=datetime.date.today)
    content = MartorField()
    link = models.CharField(max_length=200, default="https://suraudata.xyz")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']