"""
Tests for the models
"""

from django.test import TestCase #baseClass for test
from django.contrib.auth import get_user_model


class TestModel(TestCase):
    """Test for Models."""

    def test_create_user_with_email_successful(self):
        """Test success for creating user with email """
        email = 'test@example.com' #@example is saved for test
        password = 'testpassword'
        user = get_user_model().objects.create_user(
                email = email,
                password = password,
        )
        self.assertEqual(user.email,email)
        #check password for checks the hash passw
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is  normalized (non case sensitive) for new users."""
        # normalised for domain to be in small case
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],

        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email , 'sample123' )
            self.assertEqual(user.email, expected)


    def test_new_user_without_email_raises_error(self):
        """Test creating user without an email raise Value Error"""
        # there must be exception handled in create_user in model and return Value error for empty email.
        with self.assertRaises(ValueError):
            # testing the method by adding empty email and see if it raises the Exception.
            get_user_model().objects.create_user('','test123')

    
    def test_create_superuser(self):
        """Testing creation of superuser"""
        user = get_user_model().objects.create_superuser(
                'test@example.com',
                'test123',
        )

        # to access admin and everything in dj admin 
        # we need both superuser and is_staff
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)