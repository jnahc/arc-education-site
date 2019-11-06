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
  password2 = models.CharField(max_length=20)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")

  def __str__(self):
    return self.name



  

