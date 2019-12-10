from django.test import TestCase,SimpleTestCase
from django.urls import reverse


# Create your tests here.

class HomepageTest(SimpleTestCase):


    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    
    def test_homepage_url_name(self):
        response = self.client.get(reverse('foosball:home'))
        self.assertEqual(response.status_code,200)