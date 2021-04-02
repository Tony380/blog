from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse
from .views import redirect
from home.models import Post
from users.forms import RegisterForm


class TestUsersApp(TestCase):


    def setUp(self):
        user = User.objects.create(username='test', email='test@gmail.com', password='passtest9876')
        Profile.objects.create(user=user)
        Post.objects.create(title='test12', content='test12', author=user)


    def test_register_view(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)


    def test_good_register_view(self):
        form = {'username': 'test1','email': 'test@gmail.com',
        'password1': 'test123test','password2': 'test123test'}
        response = self.client.post(reverse('users:register'),data=form)
        self.assertEqual(response.status_code, 302)


    def test_logout_logged_in_view(self):
        user = User.objects.get(id=1)
        self.client.force_login(user)
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)


    def test_profile_logged_out_view(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)


    def test_profile_logged_in_view(self):
        user = User.objects.get(id=1)
        self.client.force_login(user)
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
    

    def test_profile(self):
        user = User.objects.get(id=1)
        self.client.force_login(user)
        u_form = {'username': 'test9', 'email': 'test9@gmail.com', 'image': user.profile.image}
        response = self.client.post(reverse('users:profile'), data=u_form)
        self.assertEqual(response.status_code, 302)


    def test_model(self):
        self.assertEqual(str(Profile.objects.get(id=1)), 'test')
