from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class InicioTest(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get('http://127.0.0.1:8000/crudapp/acerca-de/')
        print("test1")
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        print("test2")
    def test_template_name_correct(self):
        response = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(response, 'inicio.html')
        print("test3")
    def test_template_content(self):
        response = self.client.get(reverse('inicio'))
        self.assertContains(response, 'Inicio')
        self.assertNotContains(response, 'No es la página')
        self.assertNotContains(response, '404')
        self.assertNotContains(response, 'Bad Gateway')
        print("test4")