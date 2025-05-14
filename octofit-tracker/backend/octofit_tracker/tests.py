from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "testuser@example.com",
            "name": "Test User",
            "age": 25
        }

    def test_create_user(self):
        response = self.client.post("/api/users/", self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)

    def test_get_users(self):
        self.client.post("/api/users/", self.user_data, format="json")
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
