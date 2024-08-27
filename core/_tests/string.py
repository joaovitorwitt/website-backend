# pylint: disable=protected-access, line-too-long

import unittest
from unittest import TestCase
from entities.article.article import Article

from core.string import String


class StringTestCase(TestCase):

    def test_format_title_for_url(self):
        self.assertEqual(String._format_title_for_url('This is my title'), 'this-is-my-title')
        self.assertEqual(String._format_title_for_url('  This is my title'), 'this-is-my-title')
        self.assertEqual(String._format_title_for_url('This is my title   '), 'this-is-my-title')

        article = Article(title='How Measuraments Changed Physics', description='short description', content='in the beginning', image_url='https://')
        self.assertEqual(article.__dict__['url_title'], 'how-measuraments-changed-physics')



    # dont know how to test this
    # def test_normalize_date(self):
    #     with mock.patch('datetime.datetime.now') as mock_datetime:
    #         mock_datetime.return_value = datetime(2024, 11, 4)
    #         result = String._normalize_date()

    #     breakpoint()
    #     self.assertEqual(result, "November 4, 2024")

    def test_singularize(self):
        self.assertEqual(String.singularize('glasses'), 'glass')
        self.assertEqual(String.singularize('bushes'), 'bush')
        self.assertEqual(String.singularize('boxes'), 'box')
        self.assertEqual(String.singularize('glasses'), 'glass')

        self.assertEqual(String.singularize('teeth'), 'tooth')
        self.assertEqual(String.singularize('children'), 'child')
        # self.assertEqual(String.singularize('man'), 'men')
        # self.assertEqual(String.singularize('woman'), 'women')
        self.assertEqual(String.singularize('person'), 'people')



if __name__ == "__main__":
    unittest.main()
