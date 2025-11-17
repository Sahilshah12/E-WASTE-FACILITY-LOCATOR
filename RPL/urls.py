from django.urls import path
from . import views

app_name = 'RPL'

urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('feedback/', views.feedback_view, name='feedback'),























    path('feedback/success/', views.feedback_success, name='feedback_success'),
    path('feedback/list/', views.feedback_list, name='feedback_list'),
    

]