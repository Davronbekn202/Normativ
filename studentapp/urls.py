from django.urls import path, include

from .views import (
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    add_student, student_list, delete_student, update_student, register, user_login, user_logout,

)

urlpatterns = [
    # COURSE
    path('', CourseListView.as_view(), name='course-list'),
    path('add-course/', CourseCreateView.as_view(), name='add-course'),
    path('update-course/<int:pk>/', CourseUpdateView.as_view(), name='update-course'),
    path('delete-course/<int:pk>/', CourseDeleteView.as_view(), name='delete-course'),

    # STUDENT
    path('students/', student_list, name='student-list'),
    path('add-student/', add_student, name='add-student'),
    path('delete_student/', delete_student, name='delete_student'),
    path('update_student/', update_student, name='update_student'),
    # auth
    path('register/', register, name='registration'),
    path('log-in/', user_login, name='login'),
    path('log-out/', user_logout, name='logout'),

    path('captcha/', include('captcha.urls')),
]
