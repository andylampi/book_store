from django.test import TestCase
from django.contrib.auth import get_user_model


#Unit test
class TestUser(TestCase):
    def test_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="test",
            email="test@gmail.com",
            password="ciao1234"
        )
        self.assertEquals(user.username, "test")
        self.assertEquals(user.email, "test@gmail.com")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_super_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="andy",
            email="andy@gmail.com",
            password="ciao1234"
        )
        self.assertEquals(user.username, "andy")
        self.assertEquals(user.email, "andy@gmail.com")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)
    
