from django.http import HttpResponse
from django.shortcuts import redirect, render
from jobs.forms import JobDescriptionForm

from resumes.models import Resume
from .models import JobDescription, JobApplication 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url='accounts/login')
def create_job(request):
    if request.method == 'POST':
        form = JobDescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully')
            return redirect('job_list')
    else:
        form = JobDescriptionForm()
    return render(request, 'jobs/create_job.html', {'form': form})

def jobs_list(request):
    job_descriptions = JobDescription.objects.all()
    return render(request, 'jobs/job_list.html', {'job_descriptions':job_descriptions})
    

@login_required
def apply_job(request, job_id):
    job = JobDescription.objects.get(id = job_id)
    user_resumes = Resume.objects.filter(user = request.user)

    if user_resumes.exists():
        most_recent_resume = user_resumes.first()
        JobApplication.objects.create(user=request.user, job=job, resume=most_recent_resume)

        return render(request, 'jobs/application_success.html', {'job':job})
    else:
        return render(request, 'jobs/error.html')