from django.urls import path

from . import views


urlpatterns = [
   path('', views.jobs_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('create/', views.create_job, name='create_job'),
    path('view/<int:job_id>/', views.view_job, name='view_job'),

]