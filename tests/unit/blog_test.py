from unittest import TestCase
from blog import Blog
print("Aquí estoy")
class BlogTest(TestCase):
    def test_crete_blog(self):
        b = Blog('blog', 'jose')
        self.assertEqual('blog', b.title)
        self.assertEqual('Alexander', b.author)

    
    def test_b2(self):
        b2 = Blog('Blog prueba', 'Alexander')
        b2.posts = [1, 2]
        self.assertEqual(b2.test_b2(), 'Mi blog prueba tiene 3 posts')