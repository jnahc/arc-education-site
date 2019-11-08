from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Course(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(default="")
  start_date = models.DateField()
  end_date = models.DateField()
  photo_url = models.CharField(max_length=255)
  category = models.CharField(max_length=20)
  slug = models.SlugField(unique=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
  
  def __str__(self):
    return f"{self.title}"

  def template(self):
    return f"<li>{self.title}</li>"

  def save (self, *args, **kwargs):
    self.slug=slugify(self.title)
    super(Course, self).save(*args, **kwargs)

class Purchase(models.Model):
  student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='purchases')
  

