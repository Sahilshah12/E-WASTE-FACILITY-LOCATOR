from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('setcookies/', views.set_cookies, name='set_cookies'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('success/', views.success_view, name='success_page'),
]
