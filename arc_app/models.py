from django.db import models
from arc_profile.models import Profile

# Create your models here.

class Course(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(default="")
  start_date = models.DateField()
  end_date = models.DateField()
  category = models.CharField(max_length=100)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='courses')

def __str__(self):
  return f"{self.title}"