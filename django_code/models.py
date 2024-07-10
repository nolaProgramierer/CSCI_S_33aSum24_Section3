from django.db import models


class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    student_id = models.IntegerField(blank=True)
    active = models.BooleanField(default=True)
    student_advisor = models.ForeignKey("Advisor", on_delete=models.CASCADE, null=True, related_name="advisees")

    class Meta:
        ordering = ['student_id']

    def __str__(self):
        return f'{self.lname}, {self.fname}'
    
    def highest_course_num(self):
        return max(self.courses.all(), key=lambda x: x.course_num)

    def lowest_course_num(self):
        return min(self.courses.all(), key=lambda y: y.course_num)


class Course(models.Model):
    dept = models.CharField(max_length=3)
    course_num = models.IntegerField()
    subject = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    students = models.ManyToManyField(Student, blank=True, related_name="courses")

    class Meta:
        ordering = ['dept']

    def __str__(self):
        return f'{self.dept} {self.course_num}: {self.subject}'


class Advisor(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    u_id = models.IntegerField()

    class Meta:
        ordering = ['lname']
    
    def __str__(self):
        return f'{self.lname}, {self.fname}'
    

