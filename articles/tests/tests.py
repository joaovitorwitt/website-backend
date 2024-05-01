###############################################################################
# Imports
###############################################################################
from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from articles.models import Articles

###############################################################################
# Article Creation TestCase Implementation
###############################################################################
class ArticleCreationTestCase(APITestCase):
    def test_article_creation_with_correct_data(self):
        url = reverse('create-article')
        data = {
            'title': 'Test Title',
            'content': 'The content',
            'thumbnail': 'https://api.example.com/some-random-thumbnail'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Article created successfully")

    def test_article_creation_without_thumbnail_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': '',
            'title': 'my title',
            'description': 'my description',
            'content': 'my content'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

    def test_article_creation_without_title_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': 'https://api.example.com/some-random-thumbnail',
            'title': '',
            'description': 'my description',
            'content': 'my content'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

    def test_article_creation_without_description_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': 'https://api.example.com/some-random-thumbnail',
            'title': 'my title',
            'description': '',
            'content': 'my content'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

    def test_article_creation_without_content_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': 'https://api.example.com/some-random-thumbnail',
            'title': 'my title',
            'description': 'my description',
            'content': ''
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

    def test_article_creation_max_thumbnail_size(self):
        url = reverse('create-article')
        data = {
            'thumbnail': 'THIS STRING IS 256 CHARACTERS SASAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdsa',
            'title': 'my title',
            'description': 'my description',
            'content': 'my content'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

###############################################################################
# Article Deletion TestCase Implementation
###############################################################################
class ArticleDeletionTestCase(TestCase):

    def setUp(self):
        self.article = Articles.objects.create(
            title='test title for deletion',
            description='test description for deletion',
            content='test content for deletion',
            thumbnail='https://api.example.com/some-random-image'
        )

    def test_article_deletion_returns_expected_data_and_status(self):
        url = reverse('delete-article', kwargs={'id': self.article.id})
        client = APIClient()
        response = client.delete(url)

        self.assertEqual(response.data['message'], 'article deleted')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_deletion_with_non_existent_article(self):
        article_data = {
            'title': 'some title',
            'id': 123,
            'description': 'some description',
            'content': 'some content',
            'thumbnail': 'https://api.example.com/some-random-image'
        }
        url = reverse('delete-article', kwargs={'id': article_data['id']})
        client = APIClient()
        response = client.delete(url)

        self.assertEqual(response.data['error'], 'Articles matching query does not exist.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
###############################################################################
# Article Retrieve TestCase Implementation
###############################################################################
class ArticleRetrieveTestCase(TestCase):
    
    def setUp(self):
        self.article = Articles.objects.create(
            title='article title',
            description='article description',
            content='article content',
            thumbnail='https://api.example.com/some-random-thumbnail'

        )

    def test_article_retrieve_returns_expected_data_and_status(self):
        url = reverse('single-article', kwargs={'id': self.article.id})
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.data['message'], 'article retrieved successfully')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_retrieve_with_non_existent_article_returns_error(self):
        article_data = {
            'title': 'some title',
            'id': 123,
            'description': 'some description',
            'content': 'some content',
            'thumbnail': 'https://api.example.com/some-random-image'
        }

        url = reverse('single-article', kwargs={'id': article_data['id']})
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.data['error'], 'article could not be retrieved')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

###############################################################################
# Article Update TestCase Implementation
###############################################################################
class ArticleUpdateTestCase(TestCase):
    
    def setUp(self):
        self.article = Articles.objects.create(
            title='article title',
            description='article description',
            content='article content',
            thumbnail='https://api.example.com/some-random-thumbnail'
        )

    def test_article_update_returns_expected_data_and_status(self):
        url = reverse('update-article', kwargs={'id': self.article.id})
        client = APIClient()
        response = client.put(url)

        self.assertEqual(response.data['message'], 'article updated successfully')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_update_with_article_not_found(self):
        article_data = {
            'title': 'some title',
            'id': 123,
            'description': 'some description',
            'content': 'some content',
            'thumbnail': 'https://api.example.com/some-random-image'
        }

        url = reverse('update-article', kwargs={'id': article_data['id']})
        client = APIClient()
        response = client.put(url)

        self.assertEqual(response.data['message'], 'Article not found')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        