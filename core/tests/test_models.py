from django.test import TestCase
from model_mommy import mommy


class GeeksModelTestCase(TestCase):

    def setUp(self):
        self.title = mommy.make('GeeksModel')

    def test_str(self):
        self.assertEquals(str(self.title), self.title.title)
