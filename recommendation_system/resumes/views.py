from django.shortcuts import get_object_or_404, render, redirect
from .models import Resume
from .forms import ResumeUploadForm
from django.http import HttpResponse

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.user = request.user  # Associate the resume with the logged-in user
            new_resume.save()
            return redirect('resume_list')
    else:
        form = ResumeUploadForm()
    return render(request, 'resumes/upload_resume.html', {'form': form})

def resume_list(request):
    user_resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resumes/resume_list.html', {'user_resumes': user_resumes})


def view_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    with open(resume.pdf_file.path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={resume.pdf_file.name}'
        return response
    

def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    if request.method == 'POST':
        resume.delete()
        return redirect('resume_list')
    
    return render(request, 'resumes/delete_resume.html', {'resume': resume})