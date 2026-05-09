from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Course


# =========================
# COURSE LIST
# =========================

class CourseListView(ListView):

    model = Course

    template_name = 'course/course_list.html'

    context_object_name = 'courses'


# =========================
# COURSE CREATE
# =========================

class CourseCreateView(CreateView):

    model = Course

    fields = ['title', 'description', 'price']

    template_name = 'course/add_course.html'

    success_url = reverse_lazy('course-list')


# =========================
# COURSE UPDATE
# =========================

class CourseUpdateView(UpdateView):

    model = Course

    fields = ['title', 'description', 'price']

    template_name = 'course/update_course.html'

    success_url = reverse_lazy('course-list')


# =========================
# COURSE DELETE
# =========================

class CourseDeleteView(DeleteView):

    model = Course

    template_name = 'course/delete_course.html'

    success_url = reverse_lazy('course-list')