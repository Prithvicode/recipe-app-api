""""
Tests for admin modification
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """ Test for the Admin."""

# It uses Camel Case instead of snake.
    def setUp(self):
        """Create user and Client, test clietn"""

        self.client = Client()
        self.admin_user =  get_user_model().objects.create_superuser(
            email = 'admin@example.com',
            password = 'testpass123',
        )
        # logins with the use rthat we created
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email  = 'user@example.com',
            password = 'testpass123',
            name = 'Test User'
        )
    
    def test_users_list(self):
        """Test thta users are listed on page."""
        # {{ app_label }}_{{ model_name }}_changelist
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # check if the users we created are on the list. 
        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works."""
        url = reverse('admin:core_user_change',args =[self.user.id] )
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)

    def test_create_user_page(self):
        """Test the create user page works."""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)