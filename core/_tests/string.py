# pylint: disable=protected-access, line-too-long
import unittest
from unittest import TestCase
from entities.article.article import Article

from core.string import format_title_for_displaying, format_title_for_url


class StringTestCase(TestCase):

    def test_format_title_for_url(self):
        self.assertEqual(format_title_for_url('This is my title'), 'this-is-my-title')
        self.assertEqual(format_title_for_url('  This is my title'), 'this-is-my-title')
        self.assertEqual(format_title_for_url('This is my title   '), 'this-is-my-title')
        article = Article(title='How Measuraments Changed Physics', description='short description', content='in the beginning', image_url='https://')
        self.assertEqual(article.__dict__['url_title'], 'how-measuraments-changed-physics')

    def test_format_title_for_displaying(self):
        self.assertEqual(format_title_for_displaying('how the measurament of units changed physics forever'), 'How The Measurament Of Units Changed Physics Forever')
        self.assertEqual(format_title_for_displaying('KINEMATICS IN ONE DIMENSION'), 'Kinematics In One Dimension')
        self.assertEqual(format_title_for_displaying('the myth of the 10x developer'), 'The Myth Of The 10x Developer')
        self.assertEqual(format_title_for_displaying('how the laws of newton shape our reality'), 'How The Laws Of Newton Shape Our Reality')
        self.assertEqual(format_title_for_displaying('    perhaps    humanity will never reach the  stars  '), 'Perhaps Humanity Will Never Reach The Stars')
        article = Article(title='the myth of the 10x developer', description='short description', content='some say', image_url='https://')
        self.assertEqual(article.__dict__['title'], 'The Myth Of The 10x Developer')

    def test_normalize_date(self):
        pass

if __name__ == "__main__":
    unittest.main()
