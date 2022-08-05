from django.db import models
from datetime import datetime
# Create your models here.

class BGMI (models.Model):
  
  name = models.CharField(max_length=50)
  link = models.CharField(max_length=500)
  img = models. ImageField(upload_to='pics')
  desc = models.TextField()
  created_at = models.DateTimeField(default=datetime.now)
  price = models.IntegerField(null=True)
  
def __str__(self):
    return self.name

