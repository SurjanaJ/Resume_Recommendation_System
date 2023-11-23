from django.db import models
from django.contrib.auth.models import User

class Accounts(models.Model):
	ROLE_CHOICES = [
        ('Jobseeker', 'Jobseeker'),
        ('Employer', 'Employer'),
    ]

	account = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')


	def __str__(self):
		return self.name 
