import unittest
from django.test import TestCase,Client

# Create your tests here.
class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a POST request.
        response = self.client.post('/search_location_post/',{'keyword': 'HKU'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        print(response.data)


        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)