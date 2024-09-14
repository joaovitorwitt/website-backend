
import unittest
from unittest import TestCase, mock

from entities.article import Article

class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.article = Article(
            title='article Title',
            description='article descriptioni',
            content='some content',
            image_url='https://example.com'
        )

    def test_article_creation(self):
        pass



if __name__ == '__main__':
    unittest.main()