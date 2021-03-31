from django.urls import path
from .views import register, profile, Login, logout_view, PasswordView


urlpatterns = [
    path('register', register, name='register'),
    path('login', Login.as_view(template_name='users/login.html'), name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile, name='profile'),
    path('change_password', PasswordView.as_view(), name='change_password')
]

app_name = 'users'