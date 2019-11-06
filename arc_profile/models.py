from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  full_name = models.CharField(max_length=100)
  photo_url = models.TextField(default="https://cdn2.iconfinder.com/data/icons/gaming-and-beyond-part-2-1/80/User_gray-512.png")
  skills = models.TextField(default="")
  bio = models.TextField(default="")
  creditcard_info = models.CharField(max_length=18)
  address = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")

  def __str__(self):
    return self.name

class Course(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(default="")
  start_date = models.DateField()
  end_date = models.DateField()
  category = models.CharField(max_length=100)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='courses')

def __str__(self):
  return f"{self.title}"

  

