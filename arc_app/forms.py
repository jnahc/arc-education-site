from django import forms
from .models import Course, Purchase

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ('title', 'description', 'start_date', 'end_date', 'category', 'photo_url')


class PurchaseForm(forms.ModelForm):
  class Meta:
    model = Purchase
    fields = ('student', 'course')