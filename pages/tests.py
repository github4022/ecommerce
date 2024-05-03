from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomePageTest(SimpleTestCase):

    # def test_homepage_status_code(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_homepage_url_name(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_homepage_template(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response, 'home.html')
    #
    # def test_homepage_url_resolve_homepageview(self):
    #     view = resolve('/')
    #     self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(url)
        self.view = resolve(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_url_resolve_homepageview(self):
        self.assertEqual(self.view.func.__name__, HomePageView.as_view().__name__)
