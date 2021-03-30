from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home:index')
    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """ User's profile page with data changes possibilty"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


class Login(SuccessMessageMixin, LoginView):
    success_message = "You have been logged in successfully!"


@login_required
def logout_view(request):
    user = get_user(request)
    logout(request)
    messages.success(request, f"Good bye {user.username}! You have been logged out successfully!")
    return redirect('/')
