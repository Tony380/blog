from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from home.views import my_404_view, my_500_view
from django.conf.urls.static import static
from django.contrib.auth.views import (PasswordResetView, 
PasswordResetCompleteView, 
PasswordResetConfirmView, 
PasswordResetDoneView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include('users.urls')),
    path('password_reset', PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_complete', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]

handler404 = my_404_view
handler500 = my_500_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

