"""
Tests for user API."""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create') #return full url path 

# Helper function
def create_user(**params): #pass dictionary or any params
    """Create and return new user."""
    return get_user_model().objects.create_user(**params) 

# public tests => authentication
# ones that requires authentication

class PublicUserApiTests(TestCase):
    """Test the public features of the user API."""
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test create a user is successful."""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name' : 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED) #check if user is created
        user = get_user_model().objects.get(email = payload['email']) # after user is created we get the user 
        self.assertTrue(user.check_password(payload['password'])) # now we check if password that password matches the one we gaave it

        # security check that we are not sending back the password 
        self.assertNotIn('password',res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user iwht email exists."""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name' : 'Test Name',
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_password_too_short_error(self):
        """Test an error is returned if password less than 5 chars."""
        payload = {
            'email' : 'test@example.com',
            'password' : 'pq',
            'name' : 'TEst name',
        }
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist = get_user_model().objects.filter(
            email = payload['email']
        ).exists() # bool
        self.assertFalse(user_exist)

