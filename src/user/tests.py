from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, UserGeolocation


class SignUpViewTestCase(TestCase):
    """
    Test case for the SignUpView.
    """

    def setUp(self):
        """
        Set up the test client.
        """
        self.client = APIClient()

    def test_signup_success(self):
        """
        Test successful user signup.
        """
        url = reverse("signup")
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "password": "password123",
        }

        response = self.client.post(url, data, format="json")

        # Assert the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert a user object has been created
        self.assertEqual(User.objects.count(), 1)

        # Get the created user object
        user = User.objects.first()

        # Assert user attributes match the provided data
        self.assertEqual(user.name, data["name"])
        self.assertEqual(user.email, data["email"])
        self.assertTrue(user.check_password(data["password"]))

    def test_signup_missing_name_data(self):
        """
        Test signup with missing name data.
        """
        url = reverse("signup")
        data = {
            "email": "invalid_email",
            "password": "password123",
        }

        response = self.client.post(url, data, format="json")

        # Assert the response status code is HTTP 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Assert no user or user geolocation objects have been created
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(UserGeolocation.objects.count(), 0)
