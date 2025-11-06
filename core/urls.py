from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Main Pages
    path('', views.home, name='home'),
    path('locator/', views.facility_locator, name='locator'),
    path('learn/', views.learn, name='learn'),
    path('estimate/', views.estimate, name='estimate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # API Endpoints
    path('api/facilities/', views.facilities_json, name='facilities_json'),
]
