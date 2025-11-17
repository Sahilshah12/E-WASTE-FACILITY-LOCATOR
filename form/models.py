from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
