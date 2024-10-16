from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import RegisterForm, LoginForm, ProfileForm
from .models import User

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # Creating the new user
            user = User.objects.create_user(name, email, password)
            print(user.password)
            # Logging in the user
            auth_login(request, user) 
            print('User logged in:', request.user.is_authenticated)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.get(email=email)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                print('The user with {} logged in'.format(email))
                return redirect('home')
            else:
                form.add_error(None, "Invalid login credentials")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'accounts/profile.html', {
        'form': form,
        'user': user,
    })

@login_required
def logout_view(request):
    logout(request)
    print('User logged out')
    return redirect('logout')
