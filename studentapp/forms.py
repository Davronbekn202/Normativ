from django import forms
from .models import Course, Student


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'phone',
            'email',
            'course',
            'is_active'
        ]