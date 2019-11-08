from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
  title = models.CharField(max_length=20)
  description = models.TextField(default="")
  start_date = models.DateField()
  end_date = models.DateField()
  photo_url = models.TextField(default="")
  category = models.CharField(max_length=20)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

  
  def __str__(self):
    return f"{self.title}"

  def template(self):
    return f"<li>{self.title}</li>"


  

class Purchase(models.Model):
  student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='purchases')
  

