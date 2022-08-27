from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

User = get_user_model()


class TestModel(APITestCase):
    """"TestCase for user creation and for User model"""
    def test_create_user(self):
        user = User.objects.create_user(
            email="test@email.com",
            first_name="first_test",
            last_name="last_test",
            username="testuser",
            password="testpassword"
        )
        self.assertIsInstance(
            user, User,
            "'user' must be an instance of the User model."
        )
        self.assertFalse(
            user.is_admin or user.is_staff, False
        )
        self.assertEqual(
            user.__str__(), user.username
        )
        self.assertEqual(
            user.get_full_name, "first_test last_test"
        )
        self.assertEqual(
            user.get_short_name, user.first_name
        )
        self.assertEqual(
            user.has_perm("view"), True
        )
        self.assertEqual(
            user.has_module_perms("authentication"), True
        )

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="test@email.com",
            first_name="first_test",
            last_name="last_test",
            username="testuser",
            password="testpassword"
        )
        self.assertIsInstance(
            user, User,
            "'user' must be an instance of the User model."
        )
        self.assertTrue(
            user.is_admin and user.is_staff, True
        )

    def test_user_must_provide_an_email_when_register(self):
        self.assertRaises(
            ValueError,
            User.objects.create_user,
            email="",
            first_name="first_test",
            last_name="last_test",
            username="testuser",
            password="testpassword"
        )

