from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post  # add this import at the top

class PostTestCase(TestCase):
    # ...

    # add this test method to the PostTestCase
    
    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
        
        