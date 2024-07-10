from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from django.contrib import messages


from .models import Student, Advisor, Course

#---------------------------------------------
# Model forms
#---------------------------------------------
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['dept','course_num', 'subject', 'description']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'lname', 'student_id', 'student_advisor']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class AdvisorForm(ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdvisorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class CourseSelectionForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))


#---------------------------------------------
# Views
#---------------------------------------------
def index(request):
    students = Student.objects.order_by("lname").all()
    context = {"students": students}
    return render(request, "student/index.html", context)


def course_list(request):
    courses = Course.objects.all()
    return render(request, "student/course_list.html", {"courses": courses})


def course_detail(request, id):
    course = Course.objects.get(pk=id)
    return render(request, "student/course_detail.html", {"course": course})


def advisor_list(request):
    advisors = Advisor.objects.all()
    return render(request, "student/advisor_list.html", {"advisors": advisors})


def advisor_detail(request, id):
    advisor = Advisor.objects.get(pk=id)
    return render(request, "student/advisor_detail.html", {"advisor": advisor})


def add_student(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            new_student = student_form.save(commit=False)
            advisor = student_form.cleaned_data['student_advisor']
            new_student.student_advisor = advisor
            new_student.save()
            return HttpResponseRedirect(reverse("student_page", args=(new_student.id,)))
    return render(request, "student/add_student.html", {"form": StudentForm()})       


def edit_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            updated_student = form.save(commit=False)
            advisor = form.cleaned_data["student_advisor"]
            updated_student.student_advisor = advisor
            updated_student.save()
            return HttpResponseRedirect(reverse("student_page", args=(updated_student.id,)))
    form = StudentForm(instance=student)

    return render(request, "student/edit_student.html", {"form": form, "student": student})


def student_page(request, student_id):
    student = Student.objects.get(pk=student_id)
    courses = Course.objects.all()
    registered_courses = student.courses.all()
    context = {"student": student, "registered_courses": registered_courses, "courses": courses}
    return render(request, "student/student_page.html", context)


def course_page(request, course_id):
    course = Course.objects.get(pk=course_id)
    course_students = course.students.all()
    context = {"course": course, "students": course_students}
    return render(request, "student/course_page.html", context)


def new_course(request):
    if request.method == "POST":
        # Binding form data
        form = CourseForm(request.POST)
        if form.is_valid():
            course_form = form.save(commit=False)
            course_form.save()
            return HttpResponseRedirect(reverse("course_list"))
    return render(request, "student/add_course.html", {"form": CourseForm()})


def edit_course(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            updated_course = form.save()
            return HttpResponseRedirect(reverse("course_page", args=(updated_course.id,)))
    form = CourseForm(instance=course)

    return render(request, "student/edit_course.html", {"form": form, "course": course})


def remove_course(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == "POST":
        course.delete()
        return HttpResponseRedirect(reverse("course_list"))
    return render(request, "student/remove_course.html", {"course": course})


def new_advisor(request):
    if request.method == "POST":
        form = AdvisorForm(request.POST)
        if form.is_valid():
            advisor_form = form.save(commit="False")
            advisor_form.save()
            return HttpResponseRedirect(reverse("advisor_list"))
    return render(request, "student/add_advisor.html", {"form": AdvisorForm()})


def edit_advisor(request, id):
    advisor = get_object_or_404(Advisor, pk=id)
    if request.method == "POST":
        form = AdvisorForm(request.POST, instance=advisor)
        if form.is_valid():
            updated_advisor = form.save()
            return HttpResponseRedirect(reverse("advisor_detail", args=(updated_advisor.id,)))
    form = AdvisorForm(instance=advisor)
    return render(request, "student/edit_advisor.html", {"form": form, "advisor": advisor})


def add_student_to_course(request, id):
    student_obj = get_object_or_404(Student, pk=id)
    form = CourseSelectionForm()
    if request.method == "POST":
        form = CourseSelectionForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            course.students.add(student_obj)
            course.save()
            return HttpResponseRedirect(reverse('student_page', args=(student_obj.id,)))
    context = {"form": form, "student": student_obj}
    return render(request, "student/add_student_to_course.html", context)


def deactivate_student(request, id):
    student_obj = get_object_or_404(Student, pk=id)
    student_obj.active = False
    student_obj.save()
    messages.success(request, f'Student {student_obj.fname} {student_obj.lname} has been deactivated.')
    return HttpResponseRedirect(reverse('index'))
