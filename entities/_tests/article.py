
import unittest
from unittest import TestCase

from entities.article import Article

class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.article_data = {
            'title': 'the title',
            'description': 'article description',
            'content': 'article content',
            'image_url': 'https://example.com'
        }

        self.article = Article(**self.article_data)

    def test_article_creation(self):
        self.assertEqual(self.article.content, 'article content')
        self.assertEqual(self.article.url_title, 'the-title')

    def test_article_modification(self):
        self.assertEqual(self.article.description, 'article description')
        self.assertEqual(self.article.title, 'The Title')
        self.article['title'] = 'new title'
        self.assertEqual(self.article.title, 'new title')

    def test_article_representation(self):
        self.assertIsInstance(self.article, Article)

    def test_article_string(self):
        self.assertEqual(f"{self.article}", "Title: 'The Title' || Description: 'article description'")

    def test_article_length(self):
        self.assertEqual(len(self.article), 8)

    def test_article_get_item(self):
        self.assertEqual(self.article['title'], 'The Title')

    def test_article_set_item(self):
        self.assertEqual(self.article['content'], 'article content')
        self.article['content'] = 'new content'
        self.assertEqual(self.article['content'], 'new content')

if __name__ == '__main__':
    unittest.main()
