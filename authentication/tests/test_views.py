import json
from ..views import UserRegisterAPIView
from ..serializers import UserRegisterSerializer
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import test, status, serializers, exceptions

User = get_user_model()


class TestView(test.APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")

        self.data = {
            "email": "test@email.com",
            "first_name": "first_test",
            "last_name": "last_test",
            "username": "testuser",
            "password": "testpassword"
        }
        self.json_data = json.dumps(self.data)

    def test_user_can_register(self):
        response = self.client.post(
            path=self.register_url,
            data=self.json_data,
            content_type="application/json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    # def test_user_can_login(self):
    #     self.client.post(
    #         path=self.register_url,
    #         data=self.json_data,
    #         content_type="application/json"
    #     )
    #     response = self.client.post(
    #         path=self.login_url,
    #         data={
    #             "email": "test@email.com",
    #             "password": "testpassword"
    #         },
    #         content_type="application/json"
    #     )
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_201_CREATED
    #     )

    def test_user_input_validation(self):
        data = {
            "email": "invalid_email",
            "first_name": "first_test",
            "last_name": "last_test",
            "username": "",
            "password": "test"
        }
        json_data = json.dumps(data)
        response = self.client.post(
                path=self.register_url,
                data=json_data,
                content_type="application/json"
            )
        print(response.data)
        self.assertIsInstance(
            response.data["password"][0],
            exceptions.ErrorDetail
        )
        self.assertIsInstance(
            response.data["email"][0],
            exceptions.ErrorDetail
        )
        self.assertIsInstance(
            response.data["username"][0],
            exceptions.ErrorDetail
        )
