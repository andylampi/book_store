from users.forms import UserCreation
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls.base import reverse
from .forms import UserCreation

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
    

class TestRegistrationTemplate(TestCase):

    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_Template_signup(self):
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Signup")
        self.assertTemplateNotUsed(self.response, "login.html")
        self.assertNotContains(self.response, "Login")
    
    def test_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, UserCreation)
        self.assertContains(self.response, "csrfmiddleware")

        