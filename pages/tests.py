from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

class Test_View_Template(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_template_has_correct_html(self):
        self.assertContains(self.response, "HomePage")

    def test_template_has_not_correct_html(self):
        self.assertNotContains(self.response, "Hello world")

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "home.html")
    
    def test_template_not_used(self):
        self.assertTemplateNotUsed(self.response, "hello.html")

    def test_resolve_view(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )