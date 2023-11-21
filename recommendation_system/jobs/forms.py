from django import forms
from .models import JobDescription

class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ['title', 'description', 'pdf_file']

    