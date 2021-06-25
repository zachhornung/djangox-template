from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Band(models.Model):
  name = models.CharField(max_length=100)
  members = models.CharField(max_length=256)
  genre = models.CharField(max_length=100)
  reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  rating = models.IntegerField(default=0)
  
  def __str__(self):
    return self.name[:50]