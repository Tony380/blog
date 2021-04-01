from django.test import TestCase
from .models import Profile, User
from django.urls import reverse
from .views import redirect


class TestUsersViews(TestCase):


    def test_register_view(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_good_register_view(self):
        response = self.client.post(reverse('users:register'),
                                    data={'username': 'test',
                                          'email': 'test@gmail.com',
                                          'password1': 'test123test',
                                          'password2': 'test123test'})
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(redirect('index.html'))
    
    def test_bad_register_view(self):
        response = self.client.post(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')


    def test_logout_logged_in_view(self):
        user = User.objects.create(username="name")
        self.client.force_login(user)
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(redirect('index.html'))


