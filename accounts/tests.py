from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test user',
            email='testuser@ecommerce.com',
            password='testuser123',
        )
        self.assertEqual(user.username, 'test user')
        self.assertEqual(user.email, 'testuser@ecommerce.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@ecommerce.com',
            password='admin'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@ecommerce.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
