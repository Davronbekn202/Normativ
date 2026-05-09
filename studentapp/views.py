from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Course, Student
from .forms import StudentForm, RegisterForm


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


def student_list(request):

    search = request.GET.get('search')
    course_id = request.GET.get('course')

    students = Student.objects.all()
    courses = Course.objects.all()

    # SEARCH
    if search:
        students = students.filter(
            full_name__icontains=search
        ) | students.filter(
            phone__icontains=search
        ) | students.filter(
            email__icontains=search
        )

    # FILTER BY COURSE
    if course_id:
        students = students.filter(course_id=course_id)

    context = {
        'students': students,
        'courses': courses,
    }

    return render(request, 'student/student_list.html', context)


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


def delete_student(request, pk):
    # 🔥 PERMISSION CHECK
    if not request.user.groups.filter(name="Manager").exists():
        messages.error(request, "Sizga ruxsat yo‘q!")
        return redirect('student-list')

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect('student-list')

    return render(request, 'student/delete_student.html', {'student': student})


def update_student(request, pk):
    if not request.user.groups.filter(name="Manager").exists():
        return redirect('student-list')

    student = get_object_or_404(Student, pk=pk)

    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student-list')

    return render(request, 'student/update_student.html', {'form': form})


def add_students(request):
    if not request.user.groups.filter(name="Manager").exists():
        return redirect('student-list')

    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student-list')

    return render(request, 'student/add_student.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {
        'form': form,
    })




def user_login(request):

    error = None

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('student-list')

        else:
            error = "Username yoki password noto‘g‘ri"

    return render(request, 'account/login.html', {
        'error': error
    })


def user_logout(request):
    logout(request)
    return redirect('login')
