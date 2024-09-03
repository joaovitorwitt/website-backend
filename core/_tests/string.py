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


if __name__ == "__main__":
    unittest.main()
