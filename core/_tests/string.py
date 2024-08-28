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

    def test_singularize(self):
        self.assertEqual(String.singularize('glasses'), 'glass')
        self.assertEqual(String.singularize('bushes'), 'bush')
        self.assertEqual(String.singularize('boxes'), 'box')
        self.assertEqual(String.singularize('glasses'), 'glass')

        self.assertEqual(String.singularize('teeth'), 'tooth')
        self.assertEqual(String.singularize('children'), 'child')
        self.assertEqual(String.singularize('men'), 'man')
        self.assertEqual(String.singularize('women'), 'woman')
        self.assertEqual(String.singularize('person'), 'people')

        self.assertEqual(String.singularize('cities'), 'city')
        self.assertEqual(String.singularize('batteries'), 'city')
        self.assertEqual(String.singularize('industries'), 'industry')
        self.assertEqual(String.singularize('stories'), 'story')

        self.assertEqual(String.singularize('rays'), 'ray')
        self.assertEqual(String.singularize('toys'), 'toy')
        self.assertEqual(String.singularize('jerseys'), 'jersey')
        self.assertEqual(String.singularize('days'), 'day')
        self.assertEqual(String.singularize('keys'), 'key')

        self.assertEqual(String.singularize('heroes'), 'hero')
        self.assertEqual(String.singularize('potatoes'), 'potato')
        self.assertEqual(String.singularize('tomatoes'), 'tomato')

        self.assertEqual(String.singularize('deer'), 'deer')
        self.assertEqual(String.singularize('species'), 'species')
        self.assertEqual(String.singularize('series'), 'series')
        self.assertEqual(String.singularize('sheep'), 'sheep')



        

if __name__ == "__main__":
    unittest.main()
