from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Course, Student
from .forms import StudentForm, RegisterForm, LoginForm
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student-list')
    return render(request, 'student/add_student.html', {'form': form})
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course/course_list.html'
    context_object_name = 'courses'
def student_list(request):
    search = request.GET.get('search')
    course_id = request.GET.get('course')
    students = Student.objects.all()
    courses = Course.objects.all()
    if search:
        students = students.filter(
            full_name__icontains=search
        ) | students.filter(
            phone__icontains=search
        ) | students.filter(
            email__icontains=search
        )
    if course_id:
        students = students.filter(course_id=course_id)
    return render(request, 'student/student_list.html', {'students': students,'courses': courses,})
class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'description', 'price']
    template_name = 'course/add_course.html'
    success_url = reverse_lazy('course-list')
class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['title', 'description', 'price']
    template_name = 'course/update_course.html'
    success_url = reverse_lazy('course-list')
class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course/delete_course.html'
    success_url = reverse_lazy('course-list')
@login_required
def delete_student(request, pk):
    if not request.user.groups.filter(name="Manager").exists():
        messages.error(request, "Sizga ruxsat yo‘q!")
        return redirect('student-list')
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student-list')
    return render(request, 'student/delete_student.html', {'student': student})

@login_required
def update_student(request, pk):
    if not request.user.groups.filter(name="Manager").exists():
        return redirect('student-list')
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student-list')
    return render(request, 'student/update_student.html', {'form': form})


@login_required
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
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            send_mail(
                "Ro‘yxatdan o‘tish",
                "Siz kursga muvaffaqiyatli yozildingiz",
                "admin@example.com",
                [student.email],
            )
            return redirect('student-list')
    else:
        form = StudentForm()
    return render(request, 'account/register.html', {'form': form})



def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student-list')
            else:
                form.add_error(None, "Username yoki password noto‘g‘ri")
    return render(request, 'account/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
