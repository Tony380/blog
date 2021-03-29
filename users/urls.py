from django.urls import path
from .views import register, profile, Login, logout_view

urlpatterns = [
    path('register', register, name='register'),
    path('login', Login.as_view(template_name='users/login.html'), name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile, name='profile'),
    
]

app_name = 'users'