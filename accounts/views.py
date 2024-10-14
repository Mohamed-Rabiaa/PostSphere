from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from .models import User

# Create your views here.
def register(request):
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

def login(request):
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
