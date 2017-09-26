from django.db import models
from django.contrib.auth.models import User

## test api


class Grade(models.Model):
    name = models.CharField(max_length=50, null=False)
    number = models.IntegerField(null=False)
    latter = models.CharField(max_length=1, null=True)
    level = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name+' '+self.latter+' ' + self.level


class Person(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=20, null= False)
    address = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=True)
    birthdate = models.DateField(null=False)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    cellphone = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
          abstract = True



class Attorney(Person):
     # custom fields
     def __str__(self):
         return self.rut


class Student(Person):
    attorney = models.ForeignKey(Attorney, null=False, blank=True, on_delete=models.CASCADE)
    #matricula = models.ForeignKey()
    grade = models.ForeignKey(Grade, null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
         return self.rut
#
#
class Teacher(Person):
     #custom fields

     def __str__(self):
         return self.rut
#
#
# class Administrative(Person):
#     # custom fields
#
#     def __str__(self):
#         return self.rut

class Subject(models.Model):
    name = models.CharField(max_length=50, null=False)
    specialty = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.name


class Teacher_Subject(models.Model):
    subject = models.ForeignKey(Subject, null=False, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=False, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject.name+' - '+self.teacher.first_name+' '+self.teacher.last_name

class Qualification(models.Model):
    value = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    position = models.IntegerField(null=False)
    teacher_subject = models.ForeignKey(Teacher_Subject, null=False, blank=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=False, blank=True, on_delete=models.CASCADE)
    period = models.IntegerField(null=False)
    def __str__(self):
        return str(self.value)

class Enrollment(models.Model):
    rode = models.IntegerField(null=False)
    tariff = models.IntegerField(null=False)
    monthly= models.IntegerField(null=False)
    total= models.IntegerField(null=False)
    remaining= models.IntegerField(null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    grade = models.ForeignKey(Grade, null=False, blank=True, on_delete=models.CASCADE)
    period = models.IntegerField(null=False)
    student = models.ForeignKey(Student, null=False, blank=True, on_delete=models.CASCADE)

