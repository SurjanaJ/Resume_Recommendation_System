from django.contrib import admin
from .models import JobApplication, JobDescription

admin.site.register(JobDescription)
admin.site.register(JobApplication)