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

from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Student, Course


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

    # COURSE FILTER
    if course_id:
        students = students.filter(course_id=course_id)

    # PAGINATION
    paginator = Paginator(students, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'courses': courses,
    }

    return render(request, 'student/student_list.html', context)