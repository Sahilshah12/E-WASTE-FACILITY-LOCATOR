from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ClassRoom, Subject, Teacher, Student, Attendance, Mark

# admin.site.register(ClassRoom)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
# admin.site.register(Attendance)
# admin.site.register(Mark)
