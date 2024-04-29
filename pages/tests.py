# Byimaan

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # check the Http status code for the homepage equals 200 which means it exists
    def test_homepage_status_code(self):
        self.assertEqual( self.response.status_code, 200)
    
    def test_homepage_url_name(self):
        self.assertEqual( self.response.status_code, 200)

    # testing template
    def test_homepage_template(self):
        self.assertTemplateUsed( self.response, 'home.html')

    # testing Html
    def test_homepage_contains_correct_html(self):
         
        self.assertContains( self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
         
        self.assertNotContains(
             self.response, 'I should not be in html'
        )

    # Check that name of the view 'HomePageView' is used to resolve / matched HomePageView
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')

        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

    
class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correcthtml(self):
        self.assertContains(self.response, 'About page')

    def test_aboutpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'hi! this should not in the html')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )