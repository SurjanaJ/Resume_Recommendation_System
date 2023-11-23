from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from jobs.models import JobDescription
from .models import Accounts

from .forms import CreateUserForm


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            #check if user in database
            user = authenticate(request, username = username, password = password)
        
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()

                # Get the role from the form
                role = form.cleaned_data.get('role')

                # Create an associated Accounts instance
                account = Accounts.objects.create(account=user, role=role)

                # Check if the role is 'employer' and set is_superuser accordingly
                if role == 'employer':
                    user.is_superuser = True
                    user.save()

                messages.success(request, 'Account created for ' + user.username)
                return redirect('loginPage')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)

@login_required(login_url='loginPage')
def home(request):
    return render(request, 'accounts/home.html ')

@login_required(login_url='loginPage')
def profile(request):
    return render(request, 'accounts/profile.html')

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url = 'accounts/login/')
def admin_profile(request):
    admin_jobs = JobDescription.objects.filter(created_by = request.user)
    return render(request, 'accounts/admin_profile.html', {'admin_jobs': admin_jobs})
