from django.urls import path
from .views import index, Detail, Update, Delete, Create, about, DisplayUserPosts

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('display/<str:username>', DisplayUserPosts.as_view(), name='display'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
    path('update/<int:pk>', Update.as_view(), name='update'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
    path('create', Create.as_view(), name='create'),
    path('about', about, name='about'),
]

app_name = 'home'