
from unittest import TestCase
from core.string import String


class StringTestCase(TestCase):


    def test_format_title_for_url(self):
        self.assertEqual(String.format_title_for_url('This is my title'), 'this-is-my-title')
        self.assertEqual(String.format_title_for_url('  This is my title'), 'this-is-my-title')
        self.assertEqual(String.format_title_for_url('This is my title   '), 'this-is-my-title')



