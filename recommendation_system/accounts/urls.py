from django.urls import path
from . import views


urlpatterns =[
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('register/', views.register, name='register'),
    path('admin_profile/', views.admin_profile, name='admin_profile')
]