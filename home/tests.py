from django.test import TestCase
from .models import Post
from .views import Create
from users.models import Profile
from django.urls import reverse
from django.contrib.auth.models import User


class TestHomeApp(TestCase):


    def setUp(self):
        user = User.objects.create(username='test', email='test@gmail.com', password='passtest9876')
        Profile.objects.create(user=user)
        Post.objects.create(title='test12', content='test12', author=user)
        user.profile.image = 'default.png'


    def test_model(self):
        self.assertEqual(str(Post.objects.get(id=1)), 'test12')
    

    def test_about_view(self):
        response = self.client.get(reverse('home:about'))
        self.assertEqual(response.status_code, 200)


    def test_404_view(self):
        response = self.client.get('/test404')
        self.assertEqual(response.status_code, 200)

    
    def test_display(self):
        user = User.objects.get(username='test')
        response = self.client.get(reverse('home:display', args=[user]))
        self.assertEqual(response.status_code, 200)

    
    def test_create(self):
        user = User.objects.get(id=1)
        self.client.force_login(user)
        u_form = {'title': 'titletest', 'content': 'testcontent'}
        response = self.client.post(reverse('home:create'), data=u_form)
        self.assertEqual(response.status_code, 302)
    

    def test_update(self):
        user = User.objects.get(id=1)
        self.client.force_login(user)
        post = user.posts.all().first().id
        u_form = {'title': 'titletest99', 'content': 'testcontent99'}
        response = self.client.post(reverse('home:update', args=[post]), data=u_form)
        self.assertEqual(response.status_code, 302)
    

    def test_delete(self):
        user = User.objects.get(id=1)
        self.client.force_login(user)
        post = user.posts.all().first().id
        response = self.client.post(reverse('home:delete', args=[post]))
        self.assertEqual(response.status_code, 302)
