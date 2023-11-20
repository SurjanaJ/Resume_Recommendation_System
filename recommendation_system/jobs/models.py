from django.db import models
from django.contrib.auth.models import User
from resumes.models import Resume

class JobDescription(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    pdf_file = models.FileField(upload_to='jobs/job_descriptions/')
    # created_by = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"