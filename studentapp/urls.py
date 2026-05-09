from django.urls import path

from .views import (
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    add_student,
    StudentListView,
)

urlpatterns = [
    # COURSE
    path('', CourseListView.as_view(), name='course-list'),
    path('add-course/', CourseCreateView.as_view(), name='add-course'),
    path('update-course/<int:pk>/', CourseUpdateView.as_view(), name='update-course'),
    path('delete-course/<int:pk>/', CourseDeleteView.as_view(), name='delete-course'),

    # STUDENT
    path('students/', StudentListView.as_view(), name='student-list'),
    path('add-student/', add_student, name='add-student'),
]