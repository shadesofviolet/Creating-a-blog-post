# Create your models here
from django.db import models
from django.conf import settings
from django.utils import timezone

   #models.model tells that our object -post is a django model and django should save it in the database
class post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title =  models.CharField(max_length = 200)
    text =  models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_data =  models.DateTimeField(blank = True , null = True)
    
    
def publish(self):
    self.published_date = timezone.now()
    self.save()
    
def __str__(self):
    return self.title
    



