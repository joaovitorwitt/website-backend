# pylint: disable=protected-access, line-too-long
import unittest
from unittest import TestCase, mock
from entities.article import Article

from core.string import format_title_for_displaying, format_title_for_url, normalize_date
from core.date import DateTime


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
        expected_data = "October 16, 2024"

        with mock.patch('core.date.DateTime.now') as mock_now:
            mock_now.return_value = DateTime(2024, 10, 16)
            result = normalize_date(mock_now.return_value)

        self.assertEqual(result, expected_data)
        

if __name__ == "__main__":
    unittest.main()
