from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home:index')
    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class Login(SuccessMessageMixin, LoginView):
    success_message = "You have been logged in successfully!"


@login_required
def logout_view(request):
    user = get_user(request)
    logout(request)
    messages.success(request, f"Good bye {user.username}! You have been logged out successfully!")
    return redirect('/')
