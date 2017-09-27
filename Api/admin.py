from django.contrib import admin
from .models import Subject, Grade, Teacher, Student, Qualification, Attorney, Teacher_Subject, Enrollment


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Teacher_Subject)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Attorney)
admin.site.register(Qualification)
admin.site.register(Enrollment)
