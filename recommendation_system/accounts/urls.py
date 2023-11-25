from django.urls import path
from . import views
from jobs.views import delete_job, update_job

urlpatterns =[
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('register/', views.register, name='register'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('delete_job/<int:job_id>/', delete_job, name='delete_job'),
    path('update_job/<int:job_id>', update_job, name='update_job'),
    path('get_candidates/<int:job_id>/', views.get_candidates, name='get_candidates'),

]