from django.contrib.auth.mixins import PermissionRequiredMixin
from django.test import TestCase
from django.urls import reverse
from django.views.generic import CreateView

from WebLib.models import Author

class AuthorListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.assertTemplateUsed('WebLib/author_list.html')


class AuthorCreate(TestCase):

    def test_view_author_correct_template(self):
        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'WebLib/author_form.html')


