from django.urls import path

from . import views


urlpatterns = [
    path('',views.jobs, name='jobs'),
    path('job/<int:pk>/', views.job, name = 'job')
]