from django.urls import path
from . import views


urlpatterns =[
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('register/', views.register, name='register')
]