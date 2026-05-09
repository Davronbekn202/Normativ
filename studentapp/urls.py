from django.urls import path

from .views import (
    course_list,
    add_course,
    update_course,
    delete_course,

    student_list,
    add_student,
)

urlpatterns = [

    # COURSE
    path('courses/', course_list, name='course-list'),
    path('add-course/', add_course, name='add-course'),
    path('update-course/<int:pk>/', update_course, name='update-course'),
    path('delete-course/<int:pk>/', delete_course, name='delete-course'),

    # STUDENT
    path('', student_list, name='student-list'),
    path('add-student/', add_student, name='add-student'),

]