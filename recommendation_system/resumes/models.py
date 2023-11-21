from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f'{self.user.username}\'s Resume'
