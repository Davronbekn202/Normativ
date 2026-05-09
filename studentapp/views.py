from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Course, Student
from .forms import StudentForm


def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('student-list')

    context = {
        'form': form
    }

    return render(request, 'student/add_student.html', context)


class CourseListView(ListView):
    model = Course
    template_name = 'course/course_list.html'
    context_object_name = 'courses'


class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'page_obj'


class CourseCreateView(CreateView):
    model = Course

    fields = ['title', 'description', 'price']

    template_name = 'course/add_course.html'

    success_url = reverse_lazy('course-list')


class CourseUpdateView(UpdateView):
    model = Course

    fields = ['title', 'description', 'price']

    template_name = 'course/update_course.html'

    success_url = reverse_lazy('course-list')


class CourseDeleteView(DeleteView):
    model = Course

    template_name = 'course/delete_course.html'

    success_url = reverse_lazy('course-list')
