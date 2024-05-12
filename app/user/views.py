"""
Views for the User API.
"""

from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Createa new user in the system."""
    serializer_class = UserSerializer
