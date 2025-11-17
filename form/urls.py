from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('students/new/', views.student_create, name='student_create'),
    path('students/', views.student_list, name='student_list'),
]
