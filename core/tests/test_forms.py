from django.test import TestCase
from core.forms import GeeksForm


class GeeksFormTestCase(TestCase):

    def setUp(self):
        self.title = 'Title 1'
        self.description = 'Description 1'

        self.fields = {
            'title': self.title,
            'description': self.description
        }

        self.form = GeeksForm(data=self.fields)

    def test_form(self):
        form1 = GeeksForm(data=self.fields)
        form1.is_valid()

