from django.contrib import admin
from .models import Course, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at')
    search_fields = ('title',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'phone',
        'email',
        'course',
        'is_active',
        'created_at'
    )

    list_filter = ('is_active', 'course')
    search_fields = ('full_name', 'phone', 'email')