from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response  = self.client.get('/blog/')

        self.assertEqual(response.status_code,200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')

        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        main_area=soup.find('div', id='main-area')
        self.assertIn('no item', main_area.text)

        post_001 = Post.objects.create(
            title="first",
            content = 'first',
        )

        post_002 = Post.objects.create(
            title="second",
            content='second',
        )
        self.assertEqual(Post.objects.count(),2)

        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)

        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)

        self.assertNotIn('no item', main_area.text)