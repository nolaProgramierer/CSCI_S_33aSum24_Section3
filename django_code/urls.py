from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("student_page/<int:student_id>", views.student_page, name="student_page"),
    path("add_student_to_course/<int:id>", views.add_student_to_course, name="add_student_to_course"),
    path("add_student", views.add_student, name="add_student"),
    path("add_course", views.new_course, name="new_course"),
    path("add_advisor", views.new_advisor, name="new_advisor"),
    path("course/<int:course_id>", views.course_page, name="course_page"), 
    path("course_list", views.course_list, name="course_list"),
    path("course_detail/<int:id>", views.course_detail, name="course_detail"),
    path("advisor_list", views.advisor_list, name="advisor_list"),
    path("advisor_detail/<int:id>", views.advisor_detail, name="advisor_detail"),
    path("deactivate_student/<int:id>", views.deactivate_student, name="deactivate_student"),
    path("edit_student/<int:id>", views.edit_student, name="edit_student"),
    path("edit_course/<int:id>", views.edit_course, name="edit_course"),
    path("edit_advisor/<int:id>", views.edit_advisor, name="edit_advisor"),
    path("remove_course/<str:id>", views.remove_course, name="remove_course")
]