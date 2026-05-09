from django.shortcuts import render, redirect, get_object_or_404

from .models import Course, Student
from .forms import CourseForm, StudentForm


# =========================
# COURSE CRUD
# =========================

def course_list(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'course/course_list.html', context)


def add_course(request):
    form = CourseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('course-list')

    context = {
        'form': form
    }

    return render(request, 'course/add_course.html', context)


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    form = CourseForm(request.POST or None, instance=course)

    if form.is_valid():
        form.save()
        return redirect('course-list')

    context = {
        'form': form
    }

    return render(request, 'course/update_course.html', context)


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('course-list')



# =========================
# STUDENT
# =========================

def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'student/student_list.html', context)


def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student-list')

    context = {
        'form': form
    }

    return render(request, 'student/add_student.html', context)

def student_list(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(
            full_name__icontains=search
        ) | Student.objects.filter(
            phone__icontains=search
        ) | Student.objects.filter(
            email__icontains=search
        )

    else:
        students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'student/student_list.html', context)