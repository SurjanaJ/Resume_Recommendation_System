from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_resume, name='upload_resume'),
    path('list/', views.resume_list, name='resume_list'),
    path('view/<int:resume_id>/', views.view_resume, name='view_resume'),
    path('delete/<int:resume_id>/', views.delete_resume, name='delete_resume'),
]
