from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(default="")
  start_date = models.DateField()
  end_date = models.DateField()
  photo_url = models.TextField(default="https://previews.123rf.com/images/jevee/jevee1606/jevee160600132/58016549-pastel-drawn-textured-background-in-blue-colors-blank-for-letter-or-greeting-card-a4-size-format-ser.jpg")
  category = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

  
  def __str__(self):
    return f"{self.title}"

  def template(self):
    return f"<li>{self.title}</li>"


  

class Purchase(models.Model):
  student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='purchases')
  

