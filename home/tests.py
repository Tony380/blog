from django.test import TestCase
from .models import Post
from users.models import User


class TestHomeModels(TestCase):

    def test_str_method(self):
        user = User.objects.create(username='test', email='test@gmail.com', password='passtest9876')
        Post.objects.create(title='test12', content='test12', author=user)
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), 'test12')

